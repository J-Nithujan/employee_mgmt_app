# File: employees_mgmt.py
# Author: Nithujan Jegatheeswaran
# Brief: This file contains all the model functions related to the table `employees` in the database
# Version: 27.03.2022

from hashlib import sha256
from decimal import Decimal
from datetime import datetime

from app.model.models import *
from sqlalchemy.sql import *
from sqlalchemy.orm import aliased
from werkzeug.datastructures import ImmutableMultiDict
from dateutil.relativedelta import relativedelta


def check_login(email: str, password: str) -> bool:
    """
    Checks the given credentials with a SQLAlchemy session query on the table `employees`

    :param email: unique field of the table `employees`
    :param password: plain text string variable
    :return: `True` if the credentials are correct, `False` otherwise
    """
    encoded: bytes = password.encode()
    hashed = sha256(encoded)
    stmt = select(Employees.email).where(Employees.email == email,
                                         Employees.password == hashed.hexdigest())
    query_result = db.session.execute(stmt).all()

    if len(query_result) == 1:
        return True
    else:
        return False


def get_employee_data(email: str) -> tuple:
    """
    Queries the table `employees` for the data related to the given email address.

    :param email: logged employee's email address
    :return: An object with equivalent to a 'namedtuple',
    containing all the data needed on the index web page
    """
    supervisor = get_supervisor(email)
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
    stmt = select(Employees.firstname, Employees.lastname, Employees.email, Employees.hiring_date,
                  Jobs.name.label('job'), Departments.name.label('department'),
                  Employees.salary, Employees.percentage). \
        join(Departments, Employees.department_id == Departments.id). \
        join(Jobs, Employees.job_id == Jobs.id). \
        where(Employees.under_contract > 0)

    employee_list = db.session.execute(stmt).all()
    return employee_list


def get_all_supervisors():
    # TODO: justify in the project file that supervisors don't have anyone above them
    stmt = select(Employees.id, Employees.firstname, Employees.lastname).where(Employees.employee_id == None,
                                                                               Employees.under_contract == 1).order_by(
        Employees.id)
    supervisors = db.session.execute(stmt).all()
    return supervisors


def add_employee(form: ImmutableMultiDict) -> list[str]:
    errors: list[str] = []
    errors = get_error_messages(form)

    if errors:
        return errors
    else:
        password = create_password(form['firstname'], form['lastname'])
        supervisor_id = form['employee_id']
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


def update_employee(form: ImmutableMultiDict, employee_id: str) -> list[str]:
    # TODO: use ORM object to modify existing entries (same comment for task)
    errors: list[str] = []
    errors = get_error_messages(form, is_new=False)

    if errors:
        return errors
    else:
        stmt = update(Employees).where(Employees.id == employee_id).values(lastname=form['lastname'], )


# Functions used only in this file
# ---------------------------------------------

def get_employee_id(email: str) -> int:
    query = select(Employees.id).where(Employees.email == email)
    query_result = db.session.execute(query).first()
    return query_result.id


def get_employee_work_time(employee_id: int) -> Decimal:
    """

    :param employee_id:
    :return:
    """
    previous_work_time_query = select(Employees.work_time).where(Employees.id == employee_id)
    query_result = db.session.execute(previous_work_time_query).first()
    return query_result['work_time']


SECONDS_IN_AN_HOUR: Decimal = Decimal(3600)


def update_employee_work_time(employee_id: int, duration) -> None:
    """

    :param employee_id:
    :param duration:
    :return:
    """
    current_work_time: Decimal = get_employee_work_time(employee_id)
    duration_seconds: int = duration.seconds
    decimal_duration: Decimal = Decimal(round((duration_seconds / SECONDS_IN_AN_HOUR), ndigits=2))
    new_total_work_time: Decimal = current_work_time + decimal_duration
    update_query = update(Employees).where(Employees.id == employee_id).values(work_time=new_total_work_time)
    db.session.execute(update_query)
    db.session.commit()


def get_supervisor(email):
    supervisor = aliased(Employees)
    stmt = select(supervisor.firstname.label('supervisor_firstname'),
                  supervisor.lastname.label('supervisor_lastname')). \
        join(supervisor, supervisor.id == Employees.employee_id). \
        where(Employees.email == email).select_from(Employees)
    query_result = db.session.execute(stmt).first()
    return query_result


def get_error_messages(form: ImmutableMultiDict, is_new: bool = True) -> list[str]:
    errors: list[str] = []

    if form['lastname'] == '':
        errors.append('Indiquer un nom')

    if is_new:
        if form['birthdate'] == '':
            errors.append('Indiquer une date de naissance')
        else:
            birthdate = datetime.strptime(form['birthdate'], '%Y-%m-%d')
            if relativedelta(datetime.now(), birthdate).years <= 16:
                errors.append('L\'âge est inférieur à 16 ans')

        if form['firstname'] == '':
            errors.append('Indiquer un prénom')

        if form['email'] == '':
            errors.append('Indiquer une adresse email')

        if form['hiring_date'] == '':
            errors.append('Indiquer une date d\'embauche')

    if form['road'] == '':
        errors.append('Indiquer une rue')

    if 'address_id' not in form:
        errors.append('Choisir un NPA Localité dans la liste')

    if 'department_id' not in form:
        errors.append('Choisir un département dans la liste')

    if 'job_id' not in form:
        errors.append('Choisir une fonction dans la liste')

    if form['salary'] == '':
        errors.append('Indiquer un salaire')
    elif not form['salary'].isdigit():
        errors.append('Indiquer un nombre pour le salaire')

    if form['percentage'] == '':
        errors.append('Indiquer un taux de travail')
    elif not form['percentage'].isdigit():
        errors.append('Indiquer un nombre pour le taux de travail')
    elif int(form['percentage']) < 0 or int(form['percentage']) > 100:
        errors.append('Indiquer un taux de travail strictement supérieur à 0 et inférieur ou égal à 100')

    return errors


def create_password(firstname: str, lastname: str) -> str:
    plain_text_pwd = (firstname + '.' + lastname).encode()
    hashed_pwd = sha256(plain_text_pwd).hexdigest()
    return hashed_pwd


FOREIGN_KEYS: list[str] = ['address_id', 'job_id', 'department_id', 'employee_id']


def check_select_inputs(form):
    select_inputs: dict = {}

    for key in FOREIGN_KEYS:
        select_inputs[key] = ''
        if form[key]:
            select_inputs[key] = form[key]

    return select_inputs
