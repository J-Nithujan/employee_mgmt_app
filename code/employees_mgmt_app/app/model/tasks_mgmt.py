# File: tasks_mgmt.py
# Author: Nithujan Jegatheeswaran
# Brief: 
# Version: 27.03.2022

"""
This module cotains all the functions designed to select or update a task.
"""


from datetime import datetime, timedelta, time

from sqlalchemy.sql import *
from werkzeug.datastructures import ImmutableMultiDict

from app.model.employees_mgmt import get_employee_id, update_employee_work_time
from app.model.models import *


def get_tasks_list(email: str) -> list[tuple]:
    """

    :param email:
    :return:
    """
    stmt = select(Tasks.id, Tasks.project, Tasks.title, Tasks.since, Tasks.until, Tasks.validation). \
        join(employee_has_task, Tasks.id == employee_has_task.c.task_id). \
        join(Employees, employee_has_task.c.employee_id == Employees.id).where(Employees.email == email)

    tasks = db.session.execute(stmt).all()
    return tasks


def add_task(form: ImmutableMultiDict[str, str], email: str) -> list[str]:
    """

    :param form:
    :param email:
    :return: A list of error messages for the task creation or updating forms,
    an empty list means that the inputs are correct
    """
    msg_list: list[str] = get_error_messages(form)

    if len(msg_list) != 0:
        return msg_list
    else:
        datetime_inputs: tuple = convert_str_to_datetime(form['since'], form['until'], form['date'])

        duration = datetime_inputs[1] - datetime_inputs[0]

        employee_id = get_employee_id(email)
        logged_employee = Employees.query.filter_by(id=employee_id).first()

        task: Tasks = Tasks(project=form['project'], title=form['title'], description=form['description'],
                            since=datetime_inputs[0], until=datetime_inputs[1], duration=duration)
        logged_employee.tasks.append(task)
        db.session.add(task)
        db.session.commit()

        update_employee_work_time(employee_id, duration)
        return msg_list


def get_selected_task(task_id) -> dict:
    """

    :param task_id:
    :return:
    """
    query = select(Tasks.id, Tasks.project, Tasks.title, Tasks.since, Tasks.until, Tasks.description).where(
        Tasks.id == task_id)
    task = db.session.execute(query).first()

    # change of the time related data to correspond to the form's input field's format
    task_dict = dict(task)
    task_dict['since'] = task['since'].strftime('%H:%M')
    task_dict['until'] = task['until'].strftime('%H:%M')
    task_dict['date'] = task['until'].strftime('%Y-%m-%d')

    return task_dict


def update_task(form: ImmutableMultiDict[str, str], task_id: int, email: str) -> list[str]:
    """

    :param form:
    :param task_id:
    :param email:
    :return:
    """
    messages: list[str] = get_error_messages(form, new_task=False)
    if messages:
        return messages
    else:
        previous_duration_query = select(Tasks.duration).where(Tasks.id == task_id)
        previous_duration: time = db.session.execute(previous_duration_query).first()[0]
        previous_duration_td: timedelta = timedelta(hours=previous_duration.hour, minutes=previous_duration.minute)

        datetime_inputs = convert_str_to_datetime(form['since'], form['until'], form['date'])
        new_duration: timedelta = datetime_inputs[1] - datetime_inputs[0]
        duration_diff = new_duration - previous_duration_td

        update_query = update(Tasks).where(Tasks.id == task_id).values(since=datetime_inputs[0],
                                                                       until=datetime_inputs[1],
                                                                       duration=new_duration,
                                                                       description=form['description'])
        db.session.execute(update_query)
        update_employee_work_time(get_employee_id(email), duration_diff)
        db.session.commit()
        return messages


# Functions used only in this file
# ---------------------------------------------

def convert_str_to_datetime(time_1: str, time_2: str, date: str) -> tuple:
    """

    :param time_1:
    :param time_2:
    :param date:
    :return:
    """
    time_1_str = date + " " + time_1
    time_2_str = date + " " + time_2

    since_dt = datetime.strptime(time_1_str, '%Y-%m-%d %H:%M')
    until_dt = datetime.strptime(time_2_str, '%Y-%m-%d %H:%M')
    return since_dt, until_dt


def get_error_messages(form: ImmutableMultiDict[str, str], new_task: bool = True) -> list[str]:
    """
    Checks the POST form's inputs for a new or updated task and returns the errors in a message list.

    :param form: POST variable sent from either 'new_task.html' or 'edit_task.html'
    :param new_task:
    :return: A list of string variables describing the errors of the form's values
    """
    messages: list[str] = []

    if new_task:
        if form['project'] == '':
            messages.append("Indiquer le nom du projet")

        if form['title'] == '':
            messages.append("Indiquer le titre de la tâche")

    if form['since'] == '':
        messages.append("Indiquer l'heure de début")

    if form['until'] == '':
        messages.append("Indiquer l'heure de fin")

    if form['date'] == '':
        messages.append("Indiquer la date")

    if messages:
        return messages
    else:
        form_datetime: tuple = convert_str_to_datetime(form['since'], form['until'], form['date'])

        duration: timedelta = form_datetime[1] - form_datetime[0]

        if duration <= timedelta(0):
            messages.append("L'heure de fin doit être supérieur à l'heure de début de la tâche")

        return messages
