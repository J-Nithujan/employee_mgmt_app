from flask_sqlalchemy import SQLAlchemy
import logging as lg
from .views import app

db = SQLAlchemy(app)
_employees: db.Table

    
def init_db(self):
    employees = db.Table('employees', db.metadata, autoload_with=db.engine)
    payslips = db.Table('payslips', db.metadata, autoload_with=db.engine)
    addresses = db.Table('addresses', db.metadata, autoload_with=db.engine)
    jobs = db.Table('jobs', db.metadata, autoload_with=db.engine)
    departments = db.Table('departments', db.metadata, autoload_with=db.engine)
    tasks = db.Table('tasks', db.metadata, autoload_with=db.engine)
    employee_has_task = db.Table('employee_has_task', db.metadata, autoload_with=db.engine)
    lg.warning('Database initialized')
