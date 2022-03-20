# File: tables.py
# Author: Nithujan Jegatheeswaran
# Brief: 
# Version: 19.03.2022

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Addresses(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    zip = db.Column(db.VARCHAR, nullable=False)
    city = db.Column(db.VARCHAR, nullable=False)


class Departments(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.VARCHAR)


class Employees(db.Model):

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
    holiday_balance = db.Column(db.DECIMAL, nullable=False)
    under_contract = db.Column(db.Boolean, nullable=False)
    work_time = db.Column(db.DECIMAL, nullable=False)
    password = db.Column(db.VARCHAR)
    employee_id = db.Column(db.Integer)
    address_id = db.Column(db.Integer, nullable=False)
    job_id = db.Column(db.Integer, nullable=False)
    department_id = db.Column(db.Integer, nullable=False)


class Employee_has_task(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    employee_id = db.Column(db.Integer, nullable=False)
    task_id = db.Column(db.Integer, nullable=False)


class Jobs(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.VARCHAR, nullable=False)


class Payslips(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    file_path = db.Column(db.VARCHAR, nullable=False)
    date = db.Column(db.DATE, nullable=False)
    employee_id = db.Column(db.Integer, nullable=False)


class Tasks(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    project = db.Column(db.VARCHAR, nullable=False)
    title = db.Column(db.VARCHAR, nullable=False)
    description = db.Column(db.TEXT, nullable=False)
    validation = db.Column(db.BOOLEAN, nullable=False)
    since = db.Column(db.DATETIME, nullable=False)
    until = db.Column(db.DATETIME, nullable=False)


# INFO: This cannot be used for inner joins
# ---
# class Tables:
#     employees: db.Table = None
#     payslips: db.Table = None
#     addresses: db.Table = None
#     jobs: db.Table = None
#     departments: db.Table = None
#     tasks: db.Table = None
#     employee_has_task: db.Table = None
#
#     def __init__(self):
#         self.employees = db.Table('employees', db.metadata, autoload_with=db.engine)
#         self.payslips = db.Table('payslips', db.metadata, autoload_with=db.engine)
#         self.addresses = db.Table('addresses', db.metadata, autoload_with=db.engine)
#         self.jobs = db.Table('jobs', db.metadata, autoload_with=db.engine)
#         self.departments = db.Table('departments', db.metadata, autoload_with=db.engine)
#         self.tasks = db.Table('tasks', db.metadata, autoload_with=db.engine)
#         self.employee_has_task = db.Table('employee_has_task', db.metadata, autoload_with=db.engine)
