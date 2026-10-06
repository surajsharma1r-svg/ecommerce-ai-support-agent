from fastapi import FastAPI
from pydantic import BaseModel

from app.agent import run_agent


app = FastAPI(
    title="ShopEase AI Support Agent",
    description="AI Customer Support Agent using RAG, Tool Calling and Agentic Workflows",
    version="1.0.0"
)


class ChatRequest(BaseModel):
    query: str


class ChatResponse(BaseModel):
    answer: str


@app.get("/")
def home():
    return {
        "message": "ShopEase AI Support Agent is running"
    }


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    answer = run_agent(request.query)

    return {
        "answer": answer
    }