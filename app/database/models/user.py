from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class User(Base):
    __tablename__ = 'users'

    login: Mapped[str] = mapped_column(String(50), unique=True)
    hash_password: Mapped[str] = mapped_column(String(300))

    profile: Mapped["Profile"] = relationship(back_populates='user')

    def __str__(self):
        return (f'User(id={self.id}, '
                f'login={self.login})')

    def __repr__(self):
        return (f'User(id={self.id}, '
                f'login={self.login})')