from sqlalchemy.orm import Session

from database import engine
from tests.start_database import start_database

if __name__ == '__main__':
    with Session(engine) as session:
        start_database()