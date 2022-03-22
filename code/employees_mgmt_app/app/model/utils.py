# File: utils.py
# Author: Nithujan Jegatheeswaran
# Brief: 
# Version: 19.03.2022
import bdb

from app.model.tables import *
from sqlalchemy.sql import *
from sqlalchemy.orm import aliased
import hashlib
from datetime import datetime


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
    query = select(Employees.firstname, Employees.lastname, Employees.birthdate, Employees.road, Addresses.zip,
                   Addresses.city, Employees.phone_number, Employees.hiring_date, Employees.percentage,
                   Departments.name.label('department'),
                   supervisor.firstname.label('supervisor_firstname'),
                   supervisor.lastname.label('supervisor_lastname')). \
        join(supervisor, supervisor.id == Employees.employee_id). \
        join(Addresses, Employees.address_id == Addresses.id). \
        join(Departments, Employees.department_id == Departments.id). \
        where(Employees.email == email)
    
    data = db.session.execute(query).all()
    return data[0]


def get_tasks(email):
    query = select(EmployeeHasTask.task_id, Tasks.project, Tasks.title, Tasks.since, Tasks.until, Tasks.validation). \
        join(EmployeeHasTask, Tasks.id == EmployeeHasTask.task_id). \
        join(Employees, EmployeeHasTask.employee_id == Employees.id).where(Employees.email == email)
    
    tasks = db.session.execute(query).all()
    return tasks


# def add_task(post, email):
#     # TODO: add work time
#     since_str = post['date'] + " " + post['since']
#     until_str = post['date'] + " " + post['until']
#
#     task = Tasks(project=post['project'], title=post['title'], description=post['description'], since=since_str,
#                  until=until_str)
#     db.session.add(task)
#
#     query = select(Employees.id).where(Employees.email == email)
#     query_result_employee_id = db.session.execute(query).first()
#     employee_id = query_result_employee_id['id']
#
#     query = select(Tasks.id).where(Tasks.project == post['project'], Tasks.title == post['title'])
#     query_result_task_id = db.session.execute(query).first()
#     task_id = query_result_task_id['id']
#
#     employee_has_task = EmployeeHasTask(employee_id=employee_id, task_id=task_id)
#     db.session.add(employee_has_task)
#     db.session.commit()
#
#
#     time_diff = (until_dt - since_dt)
#     query = update(Employees).where(Employees.id == employee_id).values(work_time=(Employees.work_time + time_diff)
#
#
# def get_payslips():
#     pass
