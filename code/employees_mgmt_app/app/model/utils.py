# File: utils.py
# Author: Nithujan Jegatheeswaran
# Brief: 
# Version: 19.03.2022
import bdb
import time

from app.model.tables import *
from sqlalchemy.sql import *
from sqlalchemy.orm import aliased
import hashlib
import datetime


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
                   Employees.salary, Departments.name.label('department'), Jobs.name.label('job'),
                   supervisor.firstname.label('supervisor_firstname'),
                   supervisor.lastname.label('supervisor_lastname')). \
        join(supervisor, supervisor.id == Employees.employee_id). \
        join(Addresses, Employees.address_id == Addresses.id). \
        join(Departments, Employees.department_id == Departments.id). \
        join(Jobs, Employees.job_id == Jobs.id). \
        where(Employees.email == email)
    
    data = db.session.execute(query).all()
    return data[0]


def get_tasks(email):
    query = select(EmployeeHasTask.task_id, Tasks.project, Tasks.title, Tasks.since, Tasks.until, Tasks.validation). \
        join(EmployeeHasTask, Tasks.id == EmployeeHasTask.task_id). \
        join(Employees, EmployeeHasTask.employee_id == Employees.id).where(Employees.email == email)
    
    tasks = db.session.execute(query).all()
    return tasks


def add_task(post, email):
    error_msg: list[str] = []
    
    if post['project'] == '':
        error_msg.append("Indiquer le nom du projet")
    
    if post['title'] == '':
        error_msg.append("Indiquer le titre de la tâche")
    
    if post['since'] == '':
        error_msg.append("Indiquer l'heure de début")
    
    if post['until'] == '':
        error_msg.append("Indiquer l'heure de fin")
    
    if post['date'] == '':
        error_msg.append("Indiquer la date")
    
    if len(error_msg) != 0:
        return error_msg
    else:
        since_str = post['date'] + " " + post['since']
        until_str = post['date'] + " " + post['until']
        
        since_dt = datetime.datetime.strptime(since_str, '%Y-%m-%d %H:%M')
        until_dt = datetime.datetime.strptime(until_str, '%Y-%m-%d %H:%M')
        
        duration = until_dt - since_dt
        
        if duration < datetime.timedelta(0):
            error_msg.append("L'heure de fin doit être supérieur à l'heure de début de la tâche")
            return error_msg
        else:
            
            task = Tasks(project=post['project'], title=post['title'], description=post['description'], since=since_str,
                         until=until_str, duration=duration)
            db.session.add(task)
            
            query = select(Employees.id).where(Employees.email == email)
            query_result_employee_id = db.session.execute(query).first()
            employee_id = query_result_employee_id['id']
            
            query = select(Tasks.id).where(Tasks.project == post['project'], Tasks.title == post['title'])
            query_result_task_id = db.session.execute(query).first()
            task_id = query_result_task_id['id']
            
            employee_has_task = EmployeeHasTask(employee_id=employee_id, task_id=task_id)
            db.session.add(employee_has_task)
            db.session.commit()
            return error_msg


def update_task(form, task_id):
    pass


def get_payslips():
    pass
