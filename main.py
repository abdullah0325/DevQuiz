from fastapi import FastAPI
from app.api.router import api_router

app = FastAPI(
    title="Quiz MCQ Generator",
    version="1.0.0",
    description="Generate MCQs using OpenAI LLMs"
)


app.include_router(api_router, prefix="/api")

