# File: addresses_mgmt.py
# Author: Nithujan Jegatheeswaran
# Brief: This file contains all the functions retrieving data from the `addresses` table
# Version: 27.03.2022

from sqlalchemy.sql import *

from app.model.models import *


def get_all_addresses() -> list[tuple]:
    """
    Get all the entries of the table `addresses`

    :return: A custom list of tuple ordered by addresses.id that contains addresses.id, addresses.zip and addresses.city
    """
    stmt = select(Addresses.id, Addresses.zip, Addresses.city).order_by(Addresses.id)
    zip_city = db.session.execute(stmt).all()
    return zip_city
