import datetime
from sqlalchemy import DATETIME, BIGINT, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class Salary(Base):
    __tablename__ = 'salaries'

    amount: Mapped[int] = mapped_column(BIGINT)
    add_date: Mapped[datetime] = mapped_column(DATETIME, default=datetime.datetime.now())

    employee_id: Mapped[int] = mapped_column(ForeignKey("employees.id"))
    employee: Mapped["Employee"] = relationship(back_populates="salary")
