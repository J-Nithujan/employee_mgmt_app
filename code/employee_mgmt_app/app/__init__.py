# File: __init__.py
# Author: Nithujan Jegatheeswaran
# Brief: init the program and the database connection
# Version: 19.03.2022

from .views import app
from .model.models import db

# Connect sqlalchemy to the app
db.init_app(app)
