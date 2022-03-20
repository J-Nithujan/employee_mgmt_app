# File: utils.py
# Author: Nithujan Jegatheeswaran
# Brief: 
# Version: 19.03.2022

from app.model.tables import *
from sqlalchemy.sql import *
from sqlalchemy.orm import aliased
import hashlib


def check_login(email: str, password: str) -> bool:
    encoded = password.encode()
    hashed = hashlib.sha256(encoded)
    stmt = select(Employees.email).where(Employees.email == email,
                                         Employees.password == hashed.hexdigest())
    result = db.session.execute(stmt).all()

    if len(result) == 1:
        return True
    else:
        return False


def get_index_data(email: str) -> list:
    supervisor = aliased(Employees)
    # TODO: select * == safe or not ?
    query = select(Employees.firstname, Employees.lastname, Employees.birthdate, Employees.road, Addresses.zip,
                   Addresses.city, Employees.phone_number, Employees.hiring_date, Employees.percentage,
                   Departments.name.label('department'),
                   supervisor.firstname.label('supervisor_firstname'),
                   supervisor.lastname.label('supervisor_lastname')).\
        join(supervisor, supervisor.id == Employees.employee_id).\
        join(Addresses, Employees.address_id == Addresses.id).\
        join(Departments, Employees.department_id == Departments.id).\
        where(Employees.email == email)

    data = db.session.execute(query).all()
    return data[0]


# TODO: get_tasks  fct
def get_tasks(email):
    query = select(Tasks.project, Tasks.title, Tasks.since, Tasks.until).\
        join(Employee_has_task, Tasks.id == Employee_has_task.task_id).\
        join(Employees, Employee_has_task.employee_id == Employees.id).where(Employees.email == email)

    tasks = db.session.execute(query).all()
    return tasks


# TODO: add_task fct
def add_task(post):
    pass
