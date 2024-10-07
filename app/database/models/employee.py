from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Employee(Base):
    __tablename__ = 'employees'

    job: Mapped[str] = mapped_column(String(32))
    workplace: Mapped[str] = mapped_column(String(32))



