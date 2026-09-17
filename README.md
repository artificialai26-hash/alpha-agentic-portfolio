# Universal Multi-Model AI Dashboard ??
> Shared Context & Firebase Agentic Memory System (100% Free Stack)

An open-source AI dashboard that allows seamless switching between top free LLMs (DeepSeek-R1, Meta Llama 3.3, Google Gemini 2.0) without losing conversation context.

## ?? Key Features
- **Zero Context-Loss Switcher:** Switch models mid-chat while retaining full conversation history.
- **Firebase Agentic Memory:** Long-term user preferences stored in Firebase Firestore.
- **Dynamic Model Router:** Automatically routes queries to optimal free models.
- **Ultra-Lightweight:** Pure HTML/JS frontend + FastAPI backend.

## ??? Tech Stack
- **Frontend:** HTML5, Tailwind CSS (via CDN), Vanilla JavaScript
- **Backend:** Python 3.12, FastAPI, OpenRouter Free API
- **Database:** Firebase Firestore (Free Tier)
- **Deployment:** Netlify (Frontend) + Render (Backend)

## ?? Quick Start
1. Clone the repo: \git clone https://github.com/your-username/multi-model-ai-dashboard.git\`n2. Install backend dependencies: \pip install -r requirements.txt\`n3. Set environment variables in \.env\\
4. Run backend: \uvicorn backend.main:app --reload\`n5. Open \rontend/index.html\ in your browser!
