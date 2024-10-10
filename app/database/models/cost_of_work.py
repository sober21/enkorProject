from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

class CostOfWork(Base):
    __tablename__ = 'costs'

    cost_per_hour: Mapped[int]
    cost_of_selected_position: Mapped[int]
    cost_of_accepted_position: Mapped[int]
    cost_of_packaged_position: Mapped[int]

    employee_id: Mapped[int] = mapped_column(ForeignKey("employees.id"))
    employee: Mapped["Employee"] = relationship(back_populates="cost")