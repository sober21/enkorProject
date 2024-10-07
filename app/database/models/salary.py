import datetime
from sqlalchemy import DATETIME, BIGINT
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Salary(Base):
    __tablename__ = 'salaries'

    amount: Mapped[int] = mapped_column(BIGINT)
    add_date: Mapped[datetime] = mapped_column(DATETIME, default=datetime.datetime.now())
