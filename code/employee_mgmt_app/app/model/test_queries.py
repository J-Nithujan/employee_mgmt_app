# File: test_queries.py
# Author: Nithujan Jegatheeswaran
# Brief: This file contains some SQLAlchemy queries that were tested and a description of the result
# Version: 30.03.2022
#
# from sqlalchemy.sql import *
#
# from app.model.models import *
#
# # To get all the employees who are not a supervisor
# employees = Employees.query.filter_by(employees=None).all()
#
# # To get all the employees who does not have a supervisor
# supervisors = Employees.query.filter_by(employee_id=None).all()
#
# # List all the employees' email and their address's zip code and city name
# stmt = select(Addresses.zip, Addresses.city, Employees.email).join(Addresses.employees)
# employees_and_their_address = db.session.execute(stmt).all()
#
# # List of employees' lastname with their department
# stmt = select(Departments.name, Employees.lastname).join(Departments.employees)
# employees_at_some_department = db.session.execute(stmt).all()
#
# # List of employees' email with the the project and title of all their task
# stmt = select(Employees.email, Tasks.project, Tasks.title).join(Employees.tasks)
# employees_tasks = db.session.execute(stmt).all()
#
# # List of employees' payslips
# stmt = select(Employees.email, Payslips.file_path).join(Employees.payslips)
# employees_payslips = db.session.execute(stmt).all()
#
# # List of employees' lastname with the job name, ordered by employees.id (ASC)
# stmt = select(Jobs.name, Employees.lastname).join(Jobs.employees).order_by(Employees.id)
# employees_at_some_jobs = db.session.execute(stmt).all()
