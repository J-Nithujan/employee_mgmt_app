# File: jobs_mgmt.py
# Author: Nithujan Jegatheeswaran
# Brief:
# Version: 28.03.2022

from app.model.models import *
from sqlalchemy.sql import *


def get_all_jobs():
    stmt = select(Jobs.id, Jobs.name).order_by(Jobs.id)
    jobs_list = db.session.execute(stmt).all()
    return jobs_list
