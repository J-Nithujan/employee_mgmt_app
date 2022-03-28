# File: models.py
# Author: Nithujan Jegatheeswaran
# Brief: This file contains all the classes for the database tables
# Version: 27.03.2022

"""
This module contains all the mapped class of the tables from database
"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Relationship table created according to the docs
employee_has_task = db.Table('employee_has_task',
                             db.Column('id', db.Integer, autoincrement=True, primary_key=True),
                             db.Column('employee_id', db.Integer, db.ForeignKey('employees.id'), primary_key=True,
                                       nullable=False),
                             db.Column('task_id', db.Integer, db.ForeignKey('tasks.id'), primary_key=True,
                                       nullable=False))


class Addresses(db.Model):
    """
    A class for the table 'addresses' in the MySQL database
    """
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    zip = db.Column(db.VARCHAR, nullable=False)
    city = db.Column(db.VARCHAR, nullable=False)


class Departments(db.Model):
    """
        A class for the table 'departments' in the MySQL database
    """
    id: db.Column = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.VARCHAR)


class Tasks(db.Model):
    """
        A class for the table 'tasks' in the MySQL database
    """
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    project = db.Column(db.VARCHAR, nullable=False)
    title = db.Column(db.VARCHAR, nullable=False)
    description = db.Column(db.TEXT, nullable=False)
    # if no default value is given the default value is NULL for SQLAlchemy
    validation = db.Column(db.BOOLEAN, default=0)
    since = db.Column(db.DATETIME, nullable=False)
    until = db.Column(db.DATETIME, nullable=False)
    duration = db.Column(db.TIME, nullable=False)


class Employees(db.Model):
    """
        A class for the table 'employees' in the MySQL database
    """
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.VARCHAR, nullable=False)
    firstname = db.Column(db.VARCHAR, nullable=False)
    lastname = db.Column(db.VARCHAR, nullable=False)
    birthdate = db.Column(db.DATE, nullable=False)
    phone_number = db.Column(db.VARCHAR)
    road = db.Column(db.VARCHAR, nullable=False)
    hiring_date = db.Column(db.DATE, nullable=False)
    percentage = db.Column(db.DECIMAL, nullable=False)
    salary = db.Column(db.DECIMAL, nullable=False)
    # if no default value is given the default value is NULL for SQLAlchemy
    holiday_balance = db.Column(db.DECIMAL, default=0.00)
    under_contract = db.Column(db.Boolean, default=1)
    work_time = db.Column(db.DECIMAL, default=0)
    password = db.Column(db.VARCHAR, nullable=False)
    employee_id = db.Column(db.Integer)
    address_id = db.Column(db.Integer, nullable=False)
    job_id = db.Column(db.Integer, nullable=False)
    department_id = db.Column(db.Integer, nullable=False)
    tasks = db.relationship('Tasks', secondary=employee_has_task, lazy='subquery',
                            backref=db.backref('employee', lazy=True))


# class EmployeeHasTask(db.Model):
#     """
#         A class for the table 'employee_has_task' in the MySQL database
#     """
#     id = db.Column(db.Integer, autoincrement=True, primary_key=True)
#     employee_id = db.Column(db.Integer, nullable=False)
#     task_id = db.Column(db.Integer, nullable=False)


class Jobs(db.Model):
    """
        A class for the table 'jobs' in the MySQL database
    """
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.VARCHAR, nullable=False)


class Payslips(db.Model):
    """
        A class for the table 'payslips' in the MySQL database
    """
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    file_path = db.Column(db.VARCHAR, nullable=False)
    date = db.Column(db.DATE, nullable=False)
    employee_id = db.Column(db.Integer, nullable=False)
