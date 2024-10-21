from datetime import datetime
import random

from sqlalchemy import select, text
from sqlalchemy.orm import Session

from database import engine
from database.models import User, Salary, Employee, Profile, Order
from database.models.base import Base
from database.crud import get_id_by_user, get_id_by_profile, get_id_by_employee, create_user
from tests.generation_users import users

if __name__ == '__main__':
    with Session(engine) as session:
        stmt = select(Order).join(Employee.order).where(Employee.profile_id==3)
        sasha = session.scalars(stmt).all()
        for order in sasha:
            print(order.order_name, order.count_positions, order.price)
        print(sasha)