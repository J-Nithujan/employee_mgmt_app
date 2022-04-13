# File: tasks_mgmt.py
# Author: Nithujan Jegatheeswaran
# Brief: This file contains all the functions related to the entries of the tasks' table of the database
# Version: 27.03.2022

"""
This module contains all the functions designed to select, add or update a task. Also update the related table
`employees`.
"""


from datetime import datetime, timedelta, time

from werkzeug.datastructures import ImmutableMultiDict

from app.model.employees_mgmt import get_employee_by_email, update_employee_work_time
from app.model.models import db, Tasks, Employees


def get_tasks_list(email: str) -> list[Tasks]:
    """
    Gets the list of task not approved yet for the employee with the given email address.
    
    :param email: email address of the employee corresponding to the task list
    :return: a list of task object
    """
    employee: Employees = Employees.query.filter_by(email=email).first()
    task_list: list[Tasks] = []
    for task in employee.tasks:
        if task.validation is False:
            task_list.append(task)
            
    return task_list


def insert_task(form: ImmutableMultiDict[str, str], email: str) -> list[str]:
    """
    Inserts a new row in the `tasks` table of the database and bind it to the employee with the given email address.
    
    :param form: form containing the task's data
    :param email: email address of the employee who did the task
    :return: A list of error messages for the task creation,
     an empty list means that the inputs are correct
    """
    msg_list: list[str] = get_error_messages(form)

    if len(msg_list) != 0:
        return msg_list
    else:
        datetime_inputs: tuple = _convert_str_to_datetime(form['since'], form['until'])
        duration: timedelta = datetime_inputs[1] - datetime_inputs[0]
        task: Tasks = Tasks(project=form['project'], title=form['title'], description=form['description'],
                            since=datetime_inputs[0], until=datetime_inputs[1], duration=duration)

        logged_employee: Tasks = get_employee_by_email(email)
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
    Update the values of an existing row in the table `tasks`.
    
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

        datetime_inputs = _convert_str_to_datetime(form['since'], form['until'])
        # Calculation of the task's duration difference
        new_duration: timedelta = datetime_inputs[1] - datetime_inputs[0]
        previous_duration: time = task.duration
        previous_duration_td: timedelta = timedelta(previous_duration.hour, previous_duration.minute)
        is_positive: bool = True

        if new_duration < previous_duration_td:
            duration_diff = new_duration - previous_duration_td
            is_positive = False
        else:
            duration_diff = previous_duration_td - new_duration

        # Update of the `Tasks` class current instance's attributes
        task.since = datetime_inputs[0]
        task.until = datetime_inputs[1]
        task.duration = new_duration
        task.description = form['description']

        update_employee_work_time(get_employee_by_email(email), duration_diff, is_positive)
        db.session.commit()
        return messages


# Functions used only in this file
# ---------------------------------------------

def _convert_str_to_datetime(time_1: str, time_2: str) -> tuple[datetime, datetime]:
    """
    Convert two `string` describing time to `datetime`.
    
    :param time_1: string value of the first time to convert, this value should be lower than time_2
    :param time_2: string value of the second time to convert
    :return: a tuple with two `datetime` variables
    """

    since_dt = datetime.strptime(time_1, '%Y-%m-%dT%H:%M')
    until_dt = datetime.strptime(time_2, '%Y-%m-%dT%H:%M')
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
        elif len(form['project']) > 45:
            messages.append("Indiquer un nom de projet de moins de 45 caractères")

        if form['title'] == '':
            messages.append("Indiquer le titre de la tâche")
        elif len(form['title']) > 45:
            messages.append("Indiquer un titre de tâche de moins de 45 caractères")

    if form['since'] == '':
        messages.append("Indiquer l'heure de début")

    if form['until'] == '':
        messages.append("Indiquer l'heure de fin")

    if messages:
        return messages
    else:
        form_datetime: tuple = _convert_str_to_datetime(form['since'], form['until'])

        duration: timedelta = form_datetime[1] - form_datetime[0]

        if duration <= timedelta(0):
            messages.append("La date et l'heure de fin doivent être supérieur à la date et l'heure de début de la tâche")

        return messages


def get_task_with_id(task_id: int) -> Tasks:
    """
    Gets the Task ORM object corresponding to the given id.
    
    :param task_id: `id` of the task to retrieve
    :return: The selected Task object
    """
    task = Tasks.query.filter_by(id=task_id).first()
    return task
