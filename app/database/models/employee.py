from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class Employee(Base):
    __tablename__ = 'employees'

    job: Mapped[str] = mapped_column(String(32))
    workplace: Mapped[str] = mapped_column(String(32))

    profile_id: Mapped[int] = mapped_column(ForeignKey("profiles.id"))
    profile: Mapped["Profile"] = relationship(back_populates="employee")
    salary: Mapped[list["Salary"]] = relationship(back_populates="employee")
    order: Mapped[list["Order"]] = relationship(back_populates="employee")



