from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base

class Profile(Base):
    __tablename__ = 'profiles'

    name: Mapped[str] = mapped_column(String(20))
    age: Mapped[int]
    job: Mapped[str] = mapped_column(String(20))
    workplace: Mapped[str] = mapped_column(String(20))