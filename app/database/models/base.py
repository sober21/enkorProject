from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from config import setting


class Base(DeclarativeBase):
    metadata = MetaData(naming_convention=setting.naming_convention)

    id: Mapped[int] = mapped_column(primary_key=True)
