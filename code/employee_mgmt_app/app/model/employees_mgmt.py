# File: employees_mgmt.py
# Author: Nithujan Jegatheeswaran
# Brief: This file contains all the model functions related to the table `employees` of the database
# Version: 27.03.2022

from decimal import Decimal
from hashlib import sha256
from datetime import datetime, timedelta
import re

from sqlalchemy.sql import *
from sqlalchemy.orm import aliased
from werkzeug.datastructures import ImmutableMultiDict
from dateutil.relativedelta import relativedelta

from app.model.models import *


def check_login(email: str, password: str) -> bool:
    """
    Checks the given credentials with a SQLAlchemy query on the table `employees`

    :param email: unique field of the table `employees`
    :param password: plain text string variable
    :return: `True` if the credentials are correct and the employee is still working for the company, `False` otherwise
    """
    encoded: bytes = password.encode()
    hashed = sha256(encoded)
    employee: Employees = Employees.query.filter_by(email=email, password=hashed.hexdigest()).first()

    if employee and employee.under_contract:
        return True
    else:
        return False


def get_employee_data(email: str) -> tuple:
    """
    Queries the table `employees` for the data related to the given email address.

    :param email: logged employee's email address
    :return: An object with equivalent to a 'namedtuple',
     containing all the data needed on the index web page.
    """
    supervisor = get_supervisor(email)
    # We need to check if the employee is a supervisor because otherwise the `employee_id` column is empty and cannot be
    # queried
    if supervisor:
        supervisor: Alias = aliased(Employees)
        stmt = select(Employees.firstname, Employees.lastname, Employees.birthdate, Employees.road, Addresses.zip,
                      Addresses.city, Employees.phone_number, Employees.hiring_date, Employees.percentage,
                      Employees.salary, Departments.name.label('department'), Jobs.name.label('job'),
                      supervisor.firstname.label('supervisor_firstname'),
                      supervisor.lastname.label('supervisor_lastname')). \
            join(supervisor, supervisor.id == Employees.employee_id). \
            join(Addresses, Employees.address_id == Addresses.id). \
            join(Departments, Employees.department_id == Departments.id). \
            join(Jobs, Employees.job_id == Jobs.id). \
            where(Employees.email == email)
    else:
        stmt = select(Employees.firstname, Employees.lastname, Employees.birthdate, Employees.road, Addresses.zip,
                      Addresses.city, Employees.phone_number, Employees.hiring_date, Employees.percentage,
                      Employees.salary, Departments.name.label('department'), Jobs.name.label('job'), ). \
            join(Addresses, Employees.address_id == Addresses.id). \
            join(Departments, Employees.department_id == Departments.id). \
            join(Jobs, Employees.job_id == Jobs.id). \
            where(Employees.email == email)

    data = db.session.execute(stmt).first()
    return data


def get_employee_list() -> list[tuple]:
    """
    Gets the list of all active employees

    :return: a tuple list of  employees under contract. Structure of the tuples: (id, lastname, firstname, birthdate,
     email, road, zip code, city, hiring_date, department's name, job's name). The list is ordered by employees' id.
    """
    stmt = select(Employees.id, Employees.firstname, Employees.lastname, Employees.birthdate, Employees.email,
                  Employees.road, Addresses.zip, Addresses.city, Employees.hiring_date,
                  Departments.name.label('department'), Jobs.name.label('job'), Employees.salary,
                  Employees.percentage).join(Addresses).join(Departments).join(Jobs).order_by(Employees.id).where(
        Employees.under_contract != 0)
    employee_list = db.session.execute(stmt).all()
    return employee_list


def get_all_supervisors() -> list[Employees]:
    """
    Gets a list of all supervisor under contract.

    :return: An employee list of supervisors who are still under contract
    """
    # TODO: justify in the project file that supervisors don't have anyone above them
    supervisor_list = Employees.query.filter_by(employee_id=None, under_contract=1).all()
    return supervisor_list


def add_employee(form: ImmutableMultiDict) -> list[str]:
    """
    A string list with all error messages if there are any errors on the `new_employee.html` form, nothing otherwise

    :param form: data of the form sent by the user about a new employee
    :return: a list of error messages concerning for the form used to add new employees
    """
    errors = get_error_messages(form)

    if errors:
        return errors
    else:
        password = create_password(form['firstname'], form['lastname'])
        supervisor_id = form['employee_id']

        # Specific check for the supervisor input on the form
        if form['employee_id'] == 'None':
            supervisor_id = None

        new_employee: Employees = Employees(email=form['email'], firstname=form['firstname'], lastname=form['lastname'],
                                            birthdate=form['birthdate'], phone_number=form['phone_number'],
                                            road=form['road'], hiring_date=form['hiring_date'],
                                            percentage=form['percentage'], salary=form['salary'], password=password,
                                            employee_id=supervisor_id, address_id=form['address_id'],
                                            job_id=form['job_id'], department_id=form['department_id'])

        db.session.add(new_employee)
        db.session.commit()

        return errors


def get_selected_employee(employee_id) -> Employees:
    """
    Get the employees object for the given employees.id

    :param employee_id: id that will be used to look for an employee
    :return: the instance of the `Employees` class with the given `id`
    """
    employee = Employees.query.filter_by(id=employee_id).first()
    return employee


def update_employee(form: ImmutableMultiDict, employee_id: int) -> list[str]:
    """
    Update an employee and commit the changes to the database. If there are errors in the form errors will be returned

    :param form: list of updated values of an employee
    :param employee_id: id of the employee that needs to be updated
    :return: a list of error that were made on the form of `edit_employee.html`
    """
    errors = get_error_messages(form, is_new=False)

    if errors:
        return errors
    else:
        employee: Employees = Employees.query.filter_by(id=employee_id).first()

        employee.firstname = form['firstname']
        employee.road = form['road']
        employee.phone_number = form['phone_number']
        employee.address_id = form['address_id']
        employee.hiring_date = datetime.strptime(form['hiring_date'], '%Y-%m-%d')
        employee.employee_id = form['employee_id']
        employee.department_id = form['department_id']
        employee.job_id = form['job_id']
        employee.salary = form['salary']
        employee.percentage = form['percentage']
        db.session.commit()


def archive_employee(employee_id: int) -> None:
    """
    Sets an employee's `under_contract` column's value to zero.

    :param employee_id: The id of the employee that will be archived
    :return:
    """
    archived_employee: Employees = Employees.query.filter_by(id=employee_id).first()
    archived_employee.under_contract = 0
    db.session.commit()


# Functions used only in this file
# ---------------------------------------------

def get_employee_by_email(email: str) -> Employees:
    """
    Gets the `Employees` object of an employee.

    :param email: used to select the employee that will be returned
    :return: an `Employees` ORM object of the selected employee
    """
    employee = Employees.query.filter_by(email=email).first()
    return employee


def get_employee_work_time(employee_id: int) -> Decimal:
    """
    Gets an employee's work_time in the database

    :param employee_id: id of the employee that will have his/her work_time retrieved
    :return: value of the column's `work_time` from the specified employee's row
    """
    previous_work_time_query = select(Employees.work_time).where(Employees.id == employee_id)
    query_result = db.session.execute(previous_work_time_query).first()
    return query_result['work_time']


SECONDS_IN_AN_HOUR: Decimal = Decimal(3600)


def update_employee_work_time(employee: Employees, duration: timedelta, positive: bool = True) -> None:
    """
    Update the employee's work time. Does NOT commit the change, do it after all your queries

    :param employee: instance of the class `Employees` that will have its work time updated
    :param duration: the timedelta value that will be added / subtracted on the employee's `work_time` column
    :param positive: indicates if the change has to be added or subtracted
    :return:
    """
    current_work_time: Decimal = employee.work_time
    duration_seconds: int = duration.seconds
    decimal_duration: Decimal = Decimal(round((duration_seconds / SECONDS_IN_AN_HOUR), ndigits=2))

    if positive:
        new_total_work_time: Decimal = current_work_time + decimal_duration
    else:
        new_total_work_time: Decimal = current_work_time - decimal_duration

    employee.work_time = new_total_work_time


def get_supervisor(email) -> tuple:
    """
    Gets the supervisor of an employee
    :param email: value that will be used to retrieve the supervisor
    :return: returns a tuple containing the supervisor's firstname and lastname
    """
    supervisor = aliased(Employees)
    stmt = select(supervisor.firstname.label('supervisor_firstname'),
                  supervisor.lastname.label('supervisor_lastname')). \
        join(supervisor, supervisor.id == Employees.employee_id). \
        where(Employees.email == email).select_from(Employees)
    query_result = db.session.execute(stmt).first()
    return query_result


# Constants used to check the salary input's value
MAX_SALARY_VALUE: int = 100_000
MIN_SALARY_VALUE: int = 1_000


def get_error_messages(form: ImmutableMultiDict, is_new: bool = True) -> list[str]:
    """
    Checks all the fields of the form on `employee_form.html`. Some checks are been made to prevent errrors in the
    database

    :param form: the form data that were sent by the user
    :param is_new: some fields will be ignored whether a new employee is added or an existing employee is updated
    :return: a list containing all the errors on the required fields of the form
    """
    errors: list[str] = []
    # Regular expression used to check if the percentage and salary inputs are numbers (decimal or integer)
    number_pattern = re.compile("^[0-9]*.?[0-9]{1,2}$")

    if form['lastname'] == '':
        errors.append('Indiquer un nom')
    elif len(form['lastname']) > 45:
        errors.append("Le nom doit faire moins de 45 caractères")

    if is_new:
        if form['birthdate'] == '':
            errors.append('Indiquer une date de naissance')
        else:
            birthdate = datetime.strptime(form['birthdate'], '%Y-%m-%d')
            if relativedelta(datetime.now(), birthdate).years <= 16:
                errors.append('L\'âge est inférieur à 16 ans')

        if form['firstname'] == '':
            errors.append('Indiquer un prénom')
        elif len(form['firstname']) > 45:
            errors.append("Le prénom doit faire moins de 45 caractères")

        if form['email'] == '':
            errors.append('Indiquer une adresse email')
        elif len(form['firstname']) > 255:
            errors.append("Le prénom doit faire moins de 255 caractères")

        if form['hiring_date'] == '':
            errors.append('Indiquer une date d\'embauche')
        elif datetime.strptime(form['hiring_date'], '%Y-%m-%d') > datetime.now():
            errors.append('Indiquer une date d\'embauche avant le jour en cours')

    if form['road'] == '':
        errors.append('Indiquer une rue')
    elif len(form['road']) > 75:
        errors.append("Le nom de rue doit faire moins de 75 caractères")

    if 'address_id' not in form:
        errors.append('Choisir un NPA Localité dans la liste')

    if 'department_id' not in form:
        errors.append('Choisir un département dans la liste')

    if 'job_id' not in form:
        errors.append('Choisir une fonction dans la liste')

    if form['salary'] == '':
        errors.append('Indiquer un salaire')
    elif not number_pattern.match(form['salary']):
        errors.append('Indiquer un nombre pour le salaire')
    elif Decimal(form['salary']) < MIN_SALARY_VALUE or Decimal(form['salary']) >= MAX_SALARY_VALUE:
        errors.append('Indiquer un salaire compris entre 100\'000 CHF et 1\'000')

    if form['percentage'] == '':
        errors.append('Indiquer un taux de travail')
    elif not number_pattern.match(form['percentage']):
        errors.append('Indiquer un nombre pour le taux de travail')
    elif Decimal(form['percentage']) < 0 or Decimal(form['percentage']) > 100:
        errors.append('Indiquer un taux de travail strictement supérieur à 0 et inférieur ou égal à 100')

    return errors


def create_password(firstname: str, lastname: str) -> str:
    """
    Function used to create a hashed password when a new employee is going to be added in the databases

    :param firstname: firstname of the employee
    :param lastname: lastname of the employee
    :return: a password hashed with sha256
    """
    plain_text_pwd = (firstname + '.' + lastname).encode()
    hashed_pwd = sha256(plain_text_pwd).hexdigest()
    return hashed_pwd
