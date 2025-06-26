from fastapi import APIRouter, Query
from typing import List
from app.schemas.mcq_schema import MCQ
from app.utils.mcqs_util import generate_mcqs

router = APIRouter()

@router.get("/", response_model=List[MCQ])
async def mcqs(language: str = Query(..., description="Programming language to generate MCQs for")):
    return generate_mcqs(language)
