# File: tasks_mgmt.py
# Author: Nithujan Jegatheeswaran
# Brief: This file contains all the functions related to the entries of the tasks' table of the database
# Version: 27.03.2022

"""
This module contains all the functions designed to select, add or update a task. Also update the related table
`empoyees`.
"""


from datetime import datetime, timedelta, time

from werkzeug.datastructures import ImmutableMultiDict

from app.model.employees_mgmt import get_employee_by_email, update_employee_work_time
from app.model.models import db, Tasks, Employees


def get_tasks_list(email: str) -> list[Tasks]:
    """
    Gets the list of not approved yet for the employee with the given email address.
    
    :param email: email address of the employee corresponding to the task list
    :return: a list of task object
    """
    employee: Employees = Employees.query.filter_by(email=email).first()
    for task in employee.tasks:
        if task.validation != 0:
            tasks_list = employee.tasks
            
    return tasks_list


def add_task(form: ImmutableMultiDict[str, str], email: str) -> list[str]:
    """
    Adds a new task to the database related to the given email address.
    
    :param form: form containing the task's data
    :param email: email address of the employee who did the task
    :return: A list of error messages for the task creation,
    an empty list means that the inputs are correct
    """
    msg_list: list[str] = get_error_messages(form)

    if len(msg_list) != 0:
        return msg_list
    else:
        datetime_inputs: tuple = convert_str_to_datetime(form['since'], form['until'], form['date'])

        duration: timedelta = datetime_inputs[1] - datetime_inputs[0]

        logged_employee: Tasks = get_employee_by_email(email)

        task: Tasks = Tasks(project=form['project'], title=form['title'], description=form['description'],
                            since=datetime_inputs[0], until=datetime_inputs[1], duration=duration)
        logged_employee.tasks.append(task)
        db.session.add(task)
        update_employee_work_time(logged_employee, duration)
        db.session.commit()
        return msg_list


def get_selected_task(task_id) -> Tasks:
    """
    Gets the task using the column `id`.
    
    :param task_id: value of the `id` column to look for
    :return: a `Tasks` object
    """
    task = Tasks.query.filter_by(id=task_id).first()
    return task


def update_task(form: ImmutableMultiDict[str, str], task_id: int, email: str) -> list[str]:
    """
    Update the values of an existing row in the `tasks` table.
    
    :param form: form containing the updated values for the task
    :param task_id: the `ìd` column's value of the task that will be updated
    :param email: the `email` column's value of the employee who did the task
    :return: a list of error messages or nothing if the form's values were valid
    """
    messages: list[str] = get_error_messages(form, new_task=False)
    if messages:
        return messages
    else:
        task: Tasks = get_task_with_id(task_id)
        
        datetime_inputs = convert_str_to_datetime(form['since'], form['until'], form['date'])
        new_duration: timedelta = datetime_inputs[1] - datetime_inputs[0]
        previous_duration: time = task.duration
        duration_diff = new_duration - timedelta(previous_duration.hour, previous_duration.minute)
        
        task.since = datetime_inputs[0]
        task.until = datetime_inputs[1]
        task.duration = new_duration
        task.description = form['description']

        update_employee_work_time(get_employee_by_email(email), duration_diff)
        db.session.commit()
        return messages


# Functions used only in this file
# ---------------------------------------------

def convert_str_to_datetime(time_1: str, time_2: str, date: str) -> tuple:
    """
    Convert two `string` describing time to `datetime`.
    
    :param time_1: string value of the first time to convert, this value should be lower than time_2
    :param time_2: string value of the second time to convert
    :param date: date that will be used to convert time_1 and time_2 from `string` to `datetime`
    :return: a tuple with two `datetime` variables
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


def get_task_with_id(task_id: int) -> Tasks:
    """
    Gets the Task ORM object corresponding to the given id.
    
    :param task_id: `id` of the task to retrieve
    :return: The selected Task object
    """
    task = Tasks.query.filter_by(id=task_id).first()
    return task
