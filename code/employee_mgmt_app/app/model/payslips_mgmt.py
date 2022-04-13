# File: payslips_mgmt.py
# Author: Nithujan Jegatheeswaran
# Brief: This file contains the function related to the payslips entries of the database
#           e.g. retrieving them in a list or creating them.
# Version: 27.03.2022

from datetime import date

from app.model.models import Payslips


def get_payslips(employee_id: int) -> list[Payslips]:
    """
    Gets an employee's payslip list
    :return: list of instances of the class `Payslips`
    """
    payslips = Payslips.query.filter_by(employee_id=employee_id).order_by(Payslips.id).all()
    return payslips


def create_payslip(employee_id: int, month_year: date) -> None:
    """
    Create the payslip of the given month and year for the specified employee
    :param employee_id: the employee which will have its payslip created
    :param month_year: the period concerned by the payslip
    :return:
    """
    # TODO: create_payslip()
    pass


# Functions used only in this file
# ---------------------------------------------

# TODO: add task scheduler
