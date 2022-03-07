from flask_sqlalchemy import SQLAlchemy
import logging as lg
from .views import app

db = SQLAlchemy(app)


class Employees(db.Model):
    
    def __init__(self):
        pass
    pass


def init_db():
    db.create_all()
    lg.warning('Database initialized')
    pass
