from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class Profile(Base):
    __tablename__ = 'profiles'

    name: Mapped[str] = mapped_column(String(20))
    age: Mapped[int]
    job: Mapped[str] = mapped_column(String(20))
    workplace: Mapped[str] = mapped_column(String(20))

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), unique=True)
    user: Mapped["User"] = relationship(back_populates="profile")
    employee: Mapped[list["Employee"]] = relationship(back_populates="profile")
