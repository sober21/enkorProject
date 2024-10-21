from sqlalchemy import select
from sqlalchemy.orm import Session, scoped_session

from database import engine
from database.models import User, Salary, Employee, Profile, Order
from database.models.base import Base


def create_user(session: Session, login: str, hash_password:str) -> User:
    user = User(login=login, hash_password=hash_password)
    session.add(user)
    session.commit()
    return user

def get_id_by_user(login: str):
    with Session(engine) as session:
        res = session.scalars(select(User.id).where(User.login==login)).first()

    return res

def get_user_by_login(login: str):
    with Session(engine) as session:
        res = session.scalars(select(User).where(User.login==login)).fetchall()

    return res