import os
from pathlib import Path

import httpx
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

load_dotenv()
BASE_DIR = Path(__file__).resolve().parent
app = FastAPI(title="BRO AI")
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")

class ChatRequest(BaseModel):
    message: str

@app.get("/")
async def home():
    return FileResponse(BASE_DIR / "static" / "index.html")

@app.post("/api/chat")
async def chat(payload: ChatRequest):
    api_key = os.getenv("AI_API_KEY", "").strip()
    api_url = os.getenv("AI_API_URL", "").strip()
    model = os.getenv("AI_MODEL", "").strip()

    if not api_key or not api_url or not model:
        return {
            "reply": "BRO is ready, but its AI brain is not connected yet. Add AI_API_KEY, AI_API_URL, and AI_MODEL to your .env file, then restart the server."
        }

    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    body = {
        "model": model,
        "messages": [
            {
                "role": "system",
                "content": "You are BRO, a helpful personal AI assistant. Be friendly, clear, safe, and useful. Help with studying, coding, and everyday questions. Do not claim to have performed actions you have not performed."
            },
            {"role": "user", "content": payload.message}
        ],
        "temperature": 0.7
    }

    try:
        async with httpx.AsyncClient(timeout=60) as client:
            response = await client.post(api_url, headers=headers, json=body)
            response.raise_for_status()
            data = response.json()
        answer = data["choices"][0]["message"]["content"]
        return {"reply": answer}
    except httpx.HTTPStatusError as exc:
        return {"reply": f"The AI provider returned an error (HTTP {exc.response.status_code}). Check your API URL, model name, and account access."}
    except (httpx.HTTPError, KeyError, IndexError, TypeError, ValueError):
        return {"reply": "I couldn't reach the AI provider. Check your internet connection and the AI settings in .env."}
