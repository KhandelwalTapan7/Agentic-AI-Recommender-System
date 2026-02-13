# 🚀 Quick Start Guide

Get up and running in under 5 minutes!

## Step 1: Backend Setup (2 minutes)

```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create environment file
cp .env.example .env

# Optional: Add your API key to .env
# (System works without it using mock data)

# Seed sample data
python seed_data.py

# Start server
python main.py
```

✅ Backend running at http://localhost:8000  
📚 API docs at http://localhost:8000/docs

## Step 2: Frontend Setup (2 minutes)

Open a **new terminal**:

```bash
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

✅ Frontend running at http://localhost:3000

## Step 3: Test It Out (1 minute)

1. Open http://localhost:3000
2. Try a sample user ID: `sales_rep_001`
3. Click "Get Recommendations"
4. See AI-generated insights! 🎉

## 🧪 What to Try

### Sample Users
- `sales_rep_001` - Sales activities
- `customer_success_001` - Support tickets
- `product_manager_001` - Feature requests

### API Testing

Visit http://localhost:8000/docs to:
- View all endpoints
- Test API calls interactively
- See request/response schemas

### Features to Explore

1. **Get Recommendations** - See AI analyze patterns
2. **View Activities** - Browse activity logs
3. **Priority Levels** - High/Medium/Low classifications
4. **Time Tracking** - See when actions happened

## 🔑 Adding Your API Key (Optional)

The system works without an API key (uses mock data), but for real AI:

1. Get an API key:
   - OpenAI: https://platform.openai.com/api-keys
   - Anthropic: https://console.anthropic.com/

2. Add to `backend/.env`:
   ```
   OPENAI_API_KEY=sk-...
   # OR
   ANTHROPIC_API_KEY=sk-ant-...
   ```

3. Restart the backend server

## 🐛 Troubleshooting

**Backend won't start?**
- Check Python version: `python --version` (need 3.9+)
- Verify virtual environment is activated
- Try: `pip install --upgrade pip` then reinstall

**Frontend won't start?**
- Check Node version: `node --version` (need 18+)
- Delete `node_modules` and run `npm install` again
- Clear npm cache: `npm cache clean --force`

**No recommendations showing?**
- Make sure backend is running on port 8000
- Check browser console for errors
- Verify user ID exists (use sample users first)

**Database errors?**
- Delete `recommendation_agent.db` file
- Run `python seed_data.py` again

## 📱 Next Steps

Once everything works:

1. ✅ Try different user IDs
2. ✅ Add your own activities via API docs
3. ✅ Customize the AI prompts in `main.py`
4. ✅ Add your own activity types in `seed_data.py`
5. ✅ Deploy to production (see README.md)

## 💡 Tips

- Keep both terminal windows open
- Backend changes require restart
- Frontend hot-reloads automatically
- Check API docs for all available endpoints
- Sample data regenerates each time you run seed_data.py

---

**Need help?** Check the full README.md or open an issue!
