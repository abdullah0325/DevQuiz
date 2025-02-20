from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import List
from utils import generate_mcqs

app = FastAPI()

class MCQResponse(BaseModel):
    question: str
    options: List[str]
    correct_answer: str

@app.get("/", response_model=List[MCQResponse])
async def mcqs(language: str ):
    """
    Generate multiple-choice questions (MCQs) for a given programming language.
    """
    return generate_mcqs(language)
    

