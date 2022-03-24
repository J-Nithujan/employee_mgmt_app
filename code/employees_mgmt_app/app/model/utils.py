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
from decimal import Decimal


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


def get_tasks_list(email):
    query = select(Tasks.id, Tasks.project, Tasks.title, Tasks.since, Tasks.until, Tasks.validation). \
        join(EmployeeHasTask, Tasks.id == EmployeeHasTask.task_id). \
        join(Employees, EmployeeHasTask.employee_id == Employees.id).where(Employees.email == email)
    
    tasks = db.session.execute(query).all()
    return tasks


def add_task(post, email) -> list[str]:
    msg_list = check_task_form(post)
    
    if len(msg_list) != 0:
        return msg_list
    else:
        form_datetime_list: tuple = convert_str_to_datetime(post['since'], post['until'], post['date'])
        
        duration: datetime.timedelta = form_datetime_list[1] - form_datetime_list[0]
        
        if duration < datetime.timedelta(0):
            msg_list.append("L'heure de fin doit être supérieur à l'heure de début de la tâche")
            return msg_list
        else:
            
            task = Tasks(project=post['project'], title=post['title'], description=post['description'],
                         since=form_datetime_list[0], until=form_datetime_list[1], duration=duration)
            db.session.add(task)
            
            query = select(Employees.id).where(Employees.email == email)
            query_result = db.session.execute(query).first()
            employee_id = query_result['id']
            update_employee_work_time(employee_id, duration)
            
            query = select(Tasks.id).where(Tasks.project == post['project'], Tasks.title == post['title'])
            query_result = db.session.execute(query).first()
            task_id = query_result['id']
            
            employee_has_task = EmployeeHasTask(employee_id=employee_id, task_id=task_id)
            db.session.add(employee_has_task)
            db.session.commit()
            return msg_list


def get_selected_task(task_id):
    query = select(Tasks.project, Tasks.title, Tasks.since, Tasks.until, Tasks.description).where(Tasks.id == task_id)
    task = db.session.execute(query).first()
    return task


def update_task(form, task_id):
    query = select(Tasks).where(Tasks.id == task_id)
    # old_duration =
    form_datetime_list = convert_str_to_datetime(form['since'], form['until'], form['date'])
    duration = None
    updated_task = Tasks(project=form['project'], title=form['title'], description=form['description'],
                         since=form_datetime_list[0], until=form_datetime_list[1], duration=duration)
    old_task = db.session.execute(query).first()
    
    pass


def get_payslips():
    pass


def check_task_form(post):
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
    
    return error_msg


def convert_str_to_datetime(time_1: str, time_2: str, date: str) -> tuple:
    time_1_str = date + " " + time_1
    time_2_str = date + " " + time_2
    
    since_dt = datetime.datetime.strptime(time_1_str, '%Y-%m-%d %H:%M')
    until_dt = datetime.datetime.strptime(time_2_str, '%Y-%m-%d %H:%M')
    return since_dt, until_dt


def get_employee_work_time(employee_id):
    query_previous_work_time = select(Employees.work_time).where(Employees.id == employee_id)
    query_result = db.session.execute(query_previous_work_time).first()
    return query_result['work_time']


SECONDS_IN_AN_HOUR: Decimal = Decimal(3600)


def update_employee_work_time(employee_id, duration):
    current_work_time = get_employee_work_time(employee_id)
    duration_seconds: int = duration.seconds
    decimal_duration: Decimal = Decimal(round((duration_seconds / SECONDS_IN_AN_HOUR), ndigits=2))
    new_total_work_time = current_work_time + decimal_duration
    query = update(Employees).where(Employees.id == employee_id).values(work_time=new_total_work_time)
    db.session.execute(query)
