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

    def __str__(self):
        return (f'Profile(id={self.id}, '
                f'name={self.name}, '
                f'age={self.age}, j'
                f'ob={self.job}, '
                f'workplace={self.workplace})')

    def __repr__(self):
        return (f'Profile(id={self.id}, '
                f'name={self.name}, '
                f'age={self.age}, '
                f'job={self.job}, '
                f'workplace={self.workplace})')