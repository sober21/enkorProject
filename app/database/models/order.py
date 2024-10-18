import datetime
from sqlalchemy import String, DATETIME, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

class Order(Base):
    __tablename__ = 'orders'

    order_name: Mapped[str] = mapped_column(String(50))
    count_positions: Mapped[int]
    price: Mapped[int]
    add_date: Mapped[datetime] = mapped_column(DATETIME, default=datetime.datetime.now())

    employee_id: Mapped[int] = mapped_column(ForeignKey("employees.id"))
    employee: Mapped["Employee"] = relationship(back_populates="order")

    def __str__(self):
        return (f'Order(order={self.order_name}, '
                f'count_position={self.count_positions}, '
                f'price={self.price}, '
                f'add_date={self.add_date})')

    def __pepr__(self):
        return (f'Order(order={self.order_name}, '
                f'count_position={self.count_positions}, '
                f'price={self.price}, '
                f'add_date={self.add_date})')