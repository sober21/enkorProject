import random
from datetime import datetime
from sqlalchemy.orm import Session

from database import engine
from database.models import User, Salary, Employee, Profile, Order
from database.models.base import Base
from database.crud import get_id_by_user, get_id_by_profile, get_id_by_employee, create_user
from tests.generation_users import users

def start_database() -> None:
    """
    Добавляет в бд 10 пользователей, каждому профиль, профиль работника, заказы и зарплату.
    :return: None
    """
    with Session(engine) as session:
        try:
            # -----------------------------регистрация
            for login, hash_password in users:
                user = create_user(session=session, login=login, hash_password=hash_password)
                session.add(user)
                session.commit()
            # ---------------------------заполнение профиля
            # тут надо знать id(pk) пользователя
            for login, hash_password in users:
                user_id = get_id_by_user(login)
                name = random.choice(['Владимир', 'Михаил', 'Александр', 'Сергей', 'Андрей', 'Дмитрий', 'Максим', 'Валентин'])
                age = random.randint(30, 57)
                job = random.choice(['Упаковщик', 'Пом. кладовщика', 'Кладовщик', 'Старший кладовщик'])
                workplace = random.choice(['Упаковка','1 отдел','3 отдел', 'Офис'])
                profile = Profile(name=name, age=age, job=job, workplace=workplace, user_id=user_id)
                session.add(profile)
                session.commit()
            # -------------------------автоматическое заполнение остальных таблиц
                profile_id = get_id_by_profile(user_id)
                employee = Employee(job=job, workplace=workplace, profile_id=profile_id)
                session.add(employee)
                session.commit()

            for i in range(100):
                em_id = random.randint(1, len(users))
                or_name = random.choice(['Москва', 'Школьников', 'ТрейдХаус'])
                count_pos = random.randint(10, 200)
                price = count_pos * 3
                order = Order(order_name=or_name, count_positions=count_pos, price=price, add_date=datetime.now(),
                              employee_id=em_id)
                salary = Salary(amount=price, add_date=datetime.now(), employee_id=em_id)
                session.add_all([order, salary])
                session.commit()
        except Exception:
            session.rollback()
            Base.metadata.drop_all(engine)