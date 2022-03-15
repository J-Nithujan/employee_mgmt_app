from app.model.tables import Tables, db
import hashlib


def check_login(email: str, password: str) -> bool:
    query_tables = Tables()
    encoded = password.encode()
    hashed = hashlib.sha256(encoded)
    result = db.session.query(query_tables.employees.c.email, query_tables.employees.c.password).select_from(
        query_tables.employees).filter(
        query_tables.employees.c.email == email, query_tables.employees.c.password == hashed.hexdigest()).all()
    if len(result) == 1:
        return True
    else:
        return False


def get_index_data(email: str) -> list[tuple]:
    query_tables: Tables = Tables()
    data: tuple = db.session.query(query_tables.employees.c.firstname, query_tables.employees.c.lastname,
                                   query_tables.employees.c.birthdate, query_tables.employees.c.road, query_tables.employees.c.phone_number, query_tables.employees.c.hiring_date, query_tables.employees.c.).select_from(query_tables.employees).filter(
        query_tables.employees.c.email == email)
    return data
    pass
