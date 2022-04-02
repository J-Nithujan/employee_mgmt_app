# File: departments_mgmt.py
# Author: Nithujan Jegatheeswaran
# Brief: This file contains all the functions retrieving data from the `departments` table
# Version: 28.03.2022


from sqlalchemy.sql import *

from app.model.models import *


def get_all_departments() -> list[tuple]:
    """
    Get a list of all rows of the table `departments`

    :return: a tuple list containing the department's id an its name
    """
    stmt = select(Departments.id, Departments.name).order_by(Departments.id)

    departments = db.session.execute(stmt).all()
    return departments
