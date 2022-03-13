from app.model.tables import Tables, db
import hashlib


def check_login(email: str, password: str) -> bool:
    query_tables = Tables()
    encoded = password.encode()
    hashed = hashlib.sha256(encoded)
    query = db.session.query(query_tables.employees.c.email, query_tables.employees.c.password).select_from(
        query_tables.employees).filter(
        query_tables.employees.c.email == email, query_tables.employees.c.password == hashed.hexdigest()).all()
    if len(query) == 1:
        return True
    else:
        return False
