from sqlalchemy.sql import *

from app.model.models import *


def test_queries():
    # Use in debug mode inside `views` or in model/ to see the result and SQL query string
    employees = Employees.query.filter_by(employees=None).all()
    supervisors = Employees.query.filter_by(employee_id=None).all()
    stmt = select(Addresses.zip, Addresses.city, Employees.email).join(Addresses.employees)
    employees_and_their_address = db.session.execute(stmt).all()
    stmt = select(Departments.name, Employees.lastname).join(Departments.employees)
    employees_at_some_department = db.session.execute(stmt).all()
    stmt = select(Employees.email, Tasks.project, Tasks.title).join(Employees.tasks)
    employees_tasks = db.session.execute(stmt).all()
    stmt = select(Employees.email, Payslips.file_path).join(Employees.payslips)
    employees_payslips = db.session.execute(stmt).all()
    stmt = select(Jobs.name, Employees.lastname).join(Jobs.employees).order_by(Employees.id)
    employees_at_some_jobs = db.session.execute(stmt).all()
