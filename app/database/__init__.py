from sqlalchemy import create_engine
from config import setting

engine = create_engine(setting.db_path, echo=True)