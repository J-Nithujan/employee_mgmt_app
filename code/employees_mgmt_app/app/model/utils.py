from app.model.tables import Tables, db
from sqlalchemy.sql import *
import hashlib


def check_login(email: str, password: str) -> bool:
    query_tables = Tables()
    employees = query_tables.employees
    encoded = password.encode()
    hashed = hashlib.sha256(encoded)
    # result = db.session.query(employees.c.email, employees.c.password).select_from(
    #     employees).filter(
    #     employees.c.email == email, employees.c.password == hashed.hexdigest()).all()
    
    stmt = select(employees.c.email, employees.c.password).where(employees.c.email == email,
                                                                 employees.c.password == hashed.hexdigest())
    with db.engine.connect() as connection:
        result = connection.execute(stmt)
    
    if len(result.all()) == 1:
        return True
    else:
        return False

# def get_index_data(email: str) -> list[tuple]:
#     # return type ????
#     query_tables: Tables = Tables()
#     data: list[tuple]  = db.session.query(query_tables.employees.c.firstname, query_tables.employees.c.lastname,
#                                    query_tables.employees.c.birthdate, query_tables.employees.c.road, query_tables.employees.c.phone_number, query_tables.employees.c.hiring_date, query_tables.employees.c.job, query_tables.employees.c.percentage).select_from(query_tables.employees).filter(
#         query_tables.employees.c.email == email)
#     return data
#     pass
