from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Tables:
    employees: db.Table = None
    payslips: db.Table = None
    addresses: db.Table = None
    jobs: db.Table = None
    departments: db.Table = None
    tasks: db.Table = None
    employee_has_task: db.Table = None

    def __init__(self):
        self.employees = db.Table('employees', db.metadata, autoload_with=db.engine)
        self.payslips = db.Table('payslips', db.metadata, autoload_with=db.engine)
        self.addresses = db.Table('addresses', db.metadata, autoload_with=db.engine)
        self.jobs = db.Table('jobs', db.metadata, autoload_with=db.engine)
        self.departments = db.Table('departments', db.metadata, autoload_with=db.engine)
        self.tasks = db.Table('tasks', db.metadata, autoload_with=db.engine)
        self.employee_has_task = db.Table('employee_has_task', db.metadata, autoload_with=db.engine)
