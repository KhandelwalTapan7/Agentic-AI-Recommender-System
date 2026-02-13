
---

# 🤖 Agentic AI Recommender System

An AI-powered recommendation engine that analyzes user activity logs and generates prioritized action suggestions using LLMs.

---

## 🚀 Features

* Activity logging system
* AI-generated recommendations
* Priority scoring
* FastAPI backend (REST API)
* Next.js 14 frontend
* SQLite database
* Clean, modern UI with Tailwind CSS

---

## 🏗️ Architecture

Frontend (Next.js) → Backend (FastAPI) → Database (SQLite) → LLM API

---

## 🛠 Tech Stack

* **Backend:** FastAPI (Python)
* **Frontend:** Next.js 14 + TypeScript
* **Database:** SQLite
* **AI:** LLM API (Groq / OpenAI compatible)
* **Styling:** Tailwind CSS

---

## ⚙️ Setup Instructions

### 1️⃣ Backend

```bash
cd backend
python -m venv venv
venv\Scripts\activate   # Windows

pip install -r requirements.txt

cp .env.example .env
# Add your API key inside .env

python seed_data.py
python main.py
```

Backend runs at:

```
http://localhost:8000
```

API docs:

```
http://localhost:8000/docs
```

---

### 2️⃣ Frontend

```bash
cd frontend
npm install
cp .env.example .env.local
npm run dev
```

Frontend runs at:

```
http://localhost:3000
```

---

## 🔌 Main API Endpoints

### Log Activity

`POST /api/activity`

```json
{
  "user_id": "user_001",
  "action": "email_opened",
  "context": "Campaign A"
}
```

### Generate Recommendations

`POST /api/recommend`

```json
{
  "user_id": "sales_rep_001",
  "limit": 5
}
```

---

## 🧠 How It Works

1. User activities are stored in the database
2. Recent activity history is analyzed
3. Data is sent to an LLM with a structured prompt
4. AI returns prioritized recommendations
5. Recommendations are saved and displayed in UI

---

## 📦 Sample Users

* `sales_rep_001`
* `customer_success_001`
* `product_manager_001`

---

## 🚢 Deployment

* Backend: Railway / Render
* Frontend: Vercel

Set environment variables before deployment.

---

## 📄 License

MIT License

---




