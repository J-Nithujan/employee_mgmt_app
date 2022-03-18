from app.model.tables import Tables, db, Employees
from sqlalchemy.sql import *
from sqlalchemy.orm import aliased
import hashlib


def check_login(email: str, password: str) -> bool:
    query_tables = Tables()
    employees = query_tables.employees
    encoded = password.encode()
    hashed = hashlib.sha256(encoded)
    # result = db.session.query(employees.c.email, employees.c.password).select_from(
    #     employees).filter(
    #     employees.c.email == email, employees.c.password == hashed.hexdigest()).all()
    
    stmt = select(Employees.email, Employees.password).where(Employees.email == email,
                                                             Employees.password == hashed.hexdigest())
    with db.engine.connect() as connection:
        result = connection.execute(stmt)
    
    if len(result.all()) == 1:
        return True
    else:
        return False


def get_index_data(email: str) -> list[tuple]:
    # return type ????
    query_tables: Tables = Tables()
    supervisor = aliased(Employees)
    # Correct this statement on the join part
    # stmt = select(Employees.first_name, Employees.last_name,
    #               Employees.birthdate, Employees.road,
    #               Employees.phone_number, Employees.hiring_date,
    #               query_tables.jobs.c.name, Employees.percentage,
    #               supervisor.first_name, supervisor.last_name).join(Employees, query_tables.jobs).join(Employees, supervisor)
    data: list = list()
    with db.engine.connect() as conn:
        for row in conn.execute(stmt):
            data = row

    # data: list[tuple] = db.session.query(query_tables.employees.c.firstname, query_tables.employees.c.lastname,
    #                                      query_tables.employees.c.birthdate, query_tables.employees.c.road,
    #                                      query_tables.employees.c.phone_number, query_tables.employees.c.hiring_date,
    #                                      query_tables.jobs.c.name, query_tables.employees.c.percentage,
    #                                      query_tables.employees.c.employee_id).select_from(
    #     query_tables.employees).join(query_tables.jobs, query_tables.employees).filter(
    #     query_tables.employees.c.email == email)
    return data
    pass
