from sqlalchemy import select
from sqlalchemy.orm import Session

from database import engine
from database.models import User


def create_user(session: Session, login: str, hash_password: str) -> User:
    user = User(login=login, hash_password=hash_password)
    session.add(user)
    session.commit()
    return user


def get_user_by_id(session: Session, user_id: int) -> User:
    with session(engine) as sess:
        stmt = select(User).where(User.id == user_id)
        user = sess.scalars(stmt).first()
    return user


def get_id_by_user(login: str):
    with Session(engine) as session:
        res = session.scalars(select(User.id).where(User.login == login)).first()

    return res


def get_user_by_login(login: str):
    with Session(engine) as session:
        res = session.scalars(select(User).where(User.login == login)).fetchall()

    return res
