# File: __init__.py
# Author: Nithujan Jegatheeswaran
# Brief: 
# Version: 19.03.2022

from .views import app
from .model.tables import db

# Connect sqlalchemy to the app
db.init_app(app)
