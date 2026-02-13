# 🤖 AI-Powered Recommendation & Prioritization Agent

An intelligent agentic system that analyzes user behavior patterns and generates actionable recommendations using AI.

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.109-green.svg)
![Next.js](https://img.shields.io/badge/Next.js-14-black.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## 🌟 Features

✅ **Behavior Analysis** - Automatically analyzes user activity logs  
✅ **AI-Powered Insights** - Generates intelligent recommendations using GPT/Claude  
✅ **Priority Scoring** - Ranks recommendations by importance  
✅ **RESTful API** - Clean FastAPI backend with full documentation  
✅ **Modern UI** - Beautiful Next.js frontend with Tailwind CSS  
✅ **Database Persistence** - SQLite/PostgreSQL for data storage  
✅ **Sample Data** - Pre-configured test scenarios for demos  

## 🏗️ Architecture

```
┌─────────────────┐
│   Next.js UI    │
│  (Port 3000)    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  FastAPI REST   │
│  (Port 8000)    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐      ┌──────────────┐
│   PostgreSQL/   │◄────►│   OpenAI/    │
│    SQLite DB    │      │  Claude API  │
└─────────────────┘      └──────────────┘
```

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| Backend   | FastAPI (Python) |
| Frontend  | Next.js 14 + TypeScript |
| Database  | PostgreSQL / SQLite |
| AI/LLM    | OpenAI GPT-4 / Anthropic Claude |
| Styling   | Tailwind CSS |
| Icons     | Lucide React |

## 🚀 Quick Start

### Prerequisites

- Python 3.9+
- Node.js 18+
- OpenAI API key OR Anthropic API key

### Backend Setup

```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env and add your API key

# Seed sample data
python seed_data.py

# Run the server
python main.py
```

The backend will be available at `http://localhost:8000`

**API Documentation:** `http://localhost:8000/docs`

### Frontend Setup

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Set up environment variables
cp .env.example .env.local

# Run development server
npm run dev
```

The frontend will be available at `http://localhost:3000`

## 📊 Sample Users

The system comes with pre-seeded test data for three user types:

1. **sales_rep_001** - Sales representative with lead follow-up activities
2. **customer_success_001** - Customer success manager with support tickets
3. **product_manager_001** - Product manager with feature requests

## 🔌 API Endpoints

### Activity Logs

**POST** `/api/activity` - Log a new activity
```json
{
  "user_id": "user_001",
  "action": "email_opened",
  "context": "Q1 campaign"
}
```

**GET** `/api/activity/{user_id}` - Get user's activity history

### Recommendations

**POST** `/api/recommend` - Generate AI recommendations
```json
{
  "user_id": "sales_rep_001",
  "limit": 10
}
```

**GET** `/api/recommendations/{user_id}` - Get stored recommendations

## 🧠 How It Works

1. **Data Collection** - User activities are logged in the database
2. **Pattern Analysis** - Recent activities are fetched and formatted
3. **AI Processing** - Activities are sent to LLM with structured prompt
4. **Recommendation Generation** - AI returns prioritized action items
5. **Storage & Display** - Recommendations are saved and shown in UI

## 🎨 Customization

### Adding New Activity Types

Edit `seed_data.py` to add your own activity patterns:

```python
SAMPLE_ACTIVITIES = {
    "your_role": [
        ("custom_action", "context details"),
        # Add more activities
    ]
}
```

### Changing AI Models

In `main.py`, modify the `call_ai_api()` function to use different models:

```python
# For Claude
"model": "claude-3-5-sonnet-20241022"

# For GPT-4
"model": "gpt-4-turbo-preview"
```

### Prompt Engineering

The recommendation prompt is in `main.py` under the `/api/recommend` endpoint. Customize it for your use case:

```python
prompt = f"""You are an intelligent recommendation engine...
[Customize this section]
"""
```

## 📈 Use Cases

This system can be adapted for:

- **Sales** - Lead prioritization and follow-up suggestions
- **Customer Success** - Churn prediction and engagement recommendations
- **Support** - Ticket escalation and workload optimization
- **Product** - Feature prioritization based on user feedback
- **Marketing** - Campaign optimization and audience targeting

## 🔧 Development

### Running Tests

```bash
# Backend tests
cd backend
pytest

# Frontend tests
cd frontend
npm test
```

### Database Migrations

```bash
# Create new migration
alembic revision --autogenerate -m "description"

# Apply migrations
alembic upgrade head
```

## 🚢 Deployment

### Backend (Railway/Render)

1. Set environment variables:
   - `OPENAI_API_KEY` or `ANTHROPIC_API_KEY`
   - `DATABASE_URL` (for PostgreSQL)

2. Deploy via Git push or CLI

### Frontend (Vercel)

1. Connect your GitHub repository
2. Set `NEXT_PUBLIC_API_URL` environment variable
3. Deploy automatically on push

## 📝 Interview Talking Points

When presenting this project:

✅ **Agentic AI** - Demonstrates autonomous decision-making  
✅ **LLM Integration** - Practical use of GPT/Claude APIs  
✅ **Full-Stack** - Complete backend + frontend implementation  
✅ **Data-Driven** - Real activity analysis with actionable outputs  
✅ **Production-Ready** - Database persistence, error handling, API docs  
✅ **Scalable** - Can handle multiple users and activity types  

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

MIT License - feel free to use this project for learning and interviews!

## 🙏 Acknowledgments

- Built for demonstrating AI engineering capabilities
- Perfect for portfolio and technical interviews
- Inspired by real-world recommendation systems

---

**Questions?** Open an issue or reach out!

**Star ⭐ this repo if it helped you!**
