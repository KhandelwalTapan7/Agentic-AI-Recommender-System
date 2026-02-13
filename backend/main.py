from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from sqlalchemy.orm import Session
import httpx
import os
import json

from models import ActivityLog, Recommendation, init_db, get_session
from dotenv import load_dotenv

load_dotenv()

print("GROQ KEY LOADED:", bool(os.getenv("GROQ_API_KEY")))

app = FastAPI(
    title="AI Recommendation Agent",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    init_db()
    print("Database initialized")


# ------------------ MODELS ------------------

class ActivityLogCreate(BaseModel):
    user_id: str
    action: str
    context: Optional[str] = None


class RecommendationRequest(BaseModel):
    user_id: str
    limit: int = 10


class RecommendationResponse(BaseModel):
    user_id: str
    recommendations: List[dict]
    analysis_timestamp: str


# ------------------ DB DEP ------------------

def get_db():
    db = get_session()
    try:
        yield db
    finally:
        db.close()


# ------------------ ROUTES ------------------

@app.get("/")
async def root():
    return {"status": "healthy"}


@app.post("/api/activity")
async def log_activity(activity: ActivityLogCreate, db: Session = Depends(get_db)):
    new_log = ActivityLog(
        user_id=activity.user_id,
        action=activity.action,
        context=activity.context,
        timestamp=datetime.utcnow()
    )
    db.add(new_log)
    db.commit()
    db.refresh(new_log)

    return {"success": True, "log": new_log.to_dict()}


@app.post("/api/recommend", response_model=RecommendationResponse)
async def generate_recommendations(
    request: RecommendationRequest,
    db: Session = Depends(get_db)
):
    activities = db.query(ActivityLog)\
        .filter(ActivityLog.user_id == request.user_id)\
        .order_by(ActivityLog.timestamp.desc())\
        .limit(request.limit)\
        .all()

    if not activities:
        raise HTTPException(status_code=404, detail="No activity found")

    activity_summary = "\n".join([
        f"- {log.timestamp.strftime('%Y-%m-%d %H:%M')}: {log.action} ({log.context or 'no context'})"
        for log in activities
    ])

    prompt = f"""
You are an intelligent business recommendation engine.

User ID: {request.user_id}

Recent Activity Logs:
{activity_summary}

Return ONLY valid JSON.
Do not include explanation text.
Do not include markdown.

Format:
{{
  "recommendations": [
    {{
      "action": "...",
      "priority": "High/Medium/Low",
      "reason": "..."
    }}
  ]
}}
"""

    try:
        ai_response = await call_groq(prompt)

        recommendations_data = extract_json(ai_response)

        if "recommendations" not in recommendations_data:
            raise Exception("Invalid AI JSON structure")

        for rec in recommendations_data["recommendations"]:
            db.add(Recommendation(
                user_id=request.user_id,
                recommendation_text=rec.get("action"),
                priority=rec.get("priority"),
                reason=rec.get("reason")
            ))

        db.commit()

        return RecommendationResponse(
            user_id=request.user_id,
            recommendations=recommendations_data["recommendations"],
            analysis_timestamp=datetime.utcnow().isoformat()
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ------------------ GROQ CALL ------------------

async def call_groq(prompt: str) -> str:
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise Exception("GROQ_API_KEY not found")

    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "llama-3.1-8b-instant",
          "messages": [
            {"role": "system", "content": "Return only valid JSON."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7,
        "max_tokens": 500
    }

    async with httpx.AsyncClient(timeout=30.0) as client:
        response = await client.post(url, headers=headers, json=payload)

        if response.status_code != 200:
            raise Exception(f"Groq API Error: {response.text}")

        result = response.json()

        return result["choices"][0]["message"]["content"]


# ------------------ JSON EXTRACT ------------------

def extract_json(response_text: str) -> dict:
    try:
        response_text = response_text.strip()

        if response_text.startswith("```"):
            response_text = response_text.split("```")[1]

        return json.loads(response_text)

    except Exception:
        return {
            "recommendations": [
                {
                    "action": "Manual review required",
                    "priority": "Medium",
                    "reason": "Failed to parse AI response"
                }
            ]
        }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)