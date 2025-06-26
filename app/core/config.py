from pydantic_settings import BaseSettings
import os 
from dotenv import load_dotenv
load_dotenv()


class Settings(BaseSettings):
    OPENAI_API_KEY: str=os.environ.get("OPENAI_API_KEY")


    class Config:
        env_file = ".env"

settings = Settings()

