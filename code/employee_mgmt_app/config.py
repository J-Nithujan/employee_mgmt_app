# File: config.py
# Author: Nithujan Jegatheeswaran
# Brief: Contains all the configuration variables for the Flask application
# Version: 27.03.2022

import random
import string

# Generate a random key for session
SECRET_KEY = ''.join([random.choice(string.printable) for _ in range(24)])

# Set to True or False to suppress error message due to future disabling
SQLALCHEMY_TRACK_MODIFICATIONS = True

# To display the interaction with the database and the program in the console
SQLALCHEMY_ECHO = True

# Specify the rdbms, the db connector used by python and the credentials used by the database
SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://employee:Pa$$w0rd@localhost/db_employees'
