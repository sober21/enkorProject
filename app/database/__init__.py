from sqlalchemy import create_engine
from config import settings

engine = create_engine(settings.db_path, echo=True)