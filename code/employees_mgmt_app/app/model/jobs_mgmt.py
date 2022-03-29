# File: jobs_mgmt.py
# Author: Nithujan Jegatheeswaran
# Brief: This file contains all the functions related to the entries of the  jobs' table of the database
# Version: 28.03.2022

from app.model.models import *
from sqlalchemy.sql import *


def get_all_jobs():
    """
    
    :return:
    """
    stmt = select(Jobs.id, Jobs.name).order_by(Jobs.id)
    jobs_list = db.session.execute(stmt).all()
    return jobs_list
