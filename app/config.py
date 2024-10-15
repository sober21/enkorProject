import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

COST_PER_HOUR_FOR_PACKER: str = os.getenv('COST_PER_HOUR_FOR_PACKER')
COST_PER_HOUR_FOR_ASSISTANT_STOREKEEPER: str = os.getenv('COST_PER_HOUR_FOR_ASSISTANT_STOREKEEPER')
COST_PER_HOUR_FOR_STOREKEEPER: str = os.getenv('COST_PER_HOUR_FOR_STOREKEEPER')
COST_OF_SELECTED_POSITION_FOR_1_DEPARTAMENT: str = os.getenv('COST_OF_SELECTED_POSITION_FOR_1_DEPARTAMENT')
COST_OF_SELECTED_POSITION_FOR_3_DEPARTAMENT: str = os.getenv('COST_OF_SELECTED_POSITION_FOR_3_DEPARTAMENT')
COST_OF_ACCEPTED_POSITION: str = os.getenv('COST_OF_ACCEPTED_POSITION')
COST_OF_PACKAGED_POSITION_FOR_PACKAGING: str = os.getenv('COST_OF_PACKAGED_POSITION_FOR_PACKAGING')
COST_OF_PACKAGED_POSITION_FOR_MAGAZINE: str = os.getenv('COST_OF_PACKAGED_POSITION_FOR_MAGAZINE')


class Settings(BaseSettings):
    db_path: str = os.getenv("DB_PATH")
    naming_convention: dict[str, str] = {
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }


settings = Settings()
