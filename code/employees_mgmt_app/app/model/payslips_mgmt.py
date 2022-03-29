# File: payslips_mgmt.py
# Author: Nithujan Jegatheeswaran
# Brief: This file contains the function related to the payslips entries of the database
#           e.g. retrieving them in a list or creating them.
# Version: 27.03.2022

from app.model.models import db, Payslips


def get_payslips(employee_id: int) -> list[Payslips]:
    """
    Gets an employee's payslip list
    :return:
    """
    payslips = Payslips.query.order_by(Payslips.id).all()
    return payslips


def create_payslips() -> None:
    # TODO: create_payslips()
    pass


# Functions used only in this file
# ---------------------------------------------
