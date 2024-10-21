from sqlalchemy import select
from sqlalchemy.orm import Session

from database import engine
from database.models import User, Salary, Employee, Profile, Order
from database.models.base import Base


def get_id_by_employee(profile_id: int):
    with Session(engine) as session:
        res = session.scalars(select(Employee.id).where(Employee.profile_id==profile_id)).first()

    return res