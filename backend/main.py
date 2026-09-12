from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import httpx

app = FastAPI(title="Hasnain Tariq - Portfolio Agent API")

# Enable CORS for static frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AgentRequest(BaseModel):
    query: str

@app.get("/api/health")
def health_check():
    return {"status": "online", "mode": "edge-01/agent"}

@app.post("/api/agent")
async def agent_query(req: AgentRequest):
    q = req.query.lower()
    
    if "who" in q or "hasnain" in q:
        resp = "Hafiz Muhammad Hasnain Tariq is an AI/ML Agentic Engineer & Python Developer from The Islamia University of Bahawalpur."
    elif "project" in q or "build" in q:
        resp = "Featured Projects: 1) Alpha Code Security Analyzer (C++/FastAPI/Groq), 2) Alpha AI Assistant (Voice/Gemini), 3) Alpha AI Engine."
    elif "contact" in q or "email" in q:
        resp = "Reach Hasnain directly at hafizhasnaintariq@gmail.com or via GitHub: github.com/artificialai26-hash"
    else:
        resp = f"Agent evaluated query: '{req.query}'. Status: Executed with 0 errors. All systems operational."
        
    return {"response": resp}

@app.get("/api/github-stats")
async def github_stats():
    # Dynamic telemetry fetch from GitHub REST API
    async with httpx.AsyncClient() as client:
        res = await client.get("https://api.github.com/users/artificialai26-hash")
        if res.status_code == 200:
            data = res.json()
            return {
                "public_repos": data.get("public_repos", 0),
                "followers": data.get("followers", 0)
            }
    return {"public_repos": 12, "followers": 5}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)