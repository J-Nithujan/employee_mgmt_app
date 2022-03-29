# File: models.py
# Author: Nithujan Jegatheeswaran
# Brief: This file contains all the classes for the database tables
# Version: 27.03.2022

from decimal import Decimal

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Relationship table created according to the docs at
# https://docs.sqlalchemy.org/en/14/orm/tutorial.html#building-a-many-to-many-relationship
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

    # one-to-many collection
    employees = db.relationship("Employees", lazy=True, backref=db.backref("address", lazy=False))


class Departments(db.Model):
    """
        A class for the table 'departments' in the MySQL database
    """
    id: db.Column = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.VARCHAR)

    employees = db.relationship("Employees", lazy=True, backref=db.backref("department", lazy=False))


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
    work_time: Decimal = db.Column(db.DECIMAL, default=0)
    password = db.Column(db.VARCHAR, nullable=False)
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'))
    address_id = db.Column(db.Integer, db.ForeignKey('addresses.id'), nullable=False)
    job_id = db.Column(db.Integer, db.ForeignKey('jobs.id'), nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'), nullable=False)
    # To get the employees list in the one to many relationship
    employees = db.relationship("Employees", remote_side=[employee_id], lazy='dynamic')
    # To get the tasks list in the many to many relationship
    tasks = db.relationship('Tasks', secondary=employee_has_task, lazy=True,
                            backref=db.backref('employee', lazy=False))
    # To get the paylsips list in the one to many relationship
    payslips = db.relationship('Payslips', lazy=True, backref=db.backref('payslips', lazy=False))


class Jobs(db.Model):
    """
        A class for the table 'jobs' in the MySQL database
    """
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.VARCHAR, nullable=False)

    employees = db.relationship("Employees", backref=db.backref("job", lazy=True))


class Payslips(db.Model):
    """
        A class for the table 'payslips' in the MySQL database
    """
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    file_path = db.Column(db.VARCHAR, nullable=False)
    date = db.Column(db.DATE, nullable=False)
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'), nullable=False)
