import os
from dotenv import load_dotenv

load_dotenv()

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    db_path: str = os.getenv("DB_PATH")



setting = Settings()