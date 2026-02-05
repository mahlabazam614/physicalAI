from fastapi import FastAPI, HTTPException, Body
from pydantic import BaseModel
from typing import List, Optional
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Physical AI Chatbot API")

class ChatRequest(BaseModel):
    message: str = ""
    history: List[dict] = []
    
class ChatResponse(BaseModel):
    reply: str
    sources: List[str] = []

@app.get("/")
def read_root():
    return {"message": "Physical AI Chatbot API is running"}

@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    # Placeholder for RAG logic
    # 1. Embed query
    # 2. Search Qdrant
    # 3. Augment prompt
    # 4. Call OpenAI
    return ChatResponse(
        reply=f"Echo: {request.message}. (RAG not yet implemented)",
        sources=["Source 1"]
    )
