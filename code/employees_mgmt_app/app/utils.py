import app
from sqlalchemy.engine import cursor
# look for connection
from models import *


def check_login(username: str, password: str) -> bool:
    with db.engine.connect() as conn:
        conn.cursor(""""
            SELECT
        """, )
