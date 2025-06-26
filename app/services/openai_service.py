from langchain_openai import ChatOpenAI
from app.core.config import settings

llm = ChatOpenAI(
    model=settings.MODEL_NAME,
    openai_api_key=settings.OPENAI_API_KEY,
    temperature=0.2
)
