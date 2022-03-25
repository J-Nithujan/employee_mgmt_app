# File: config.py
# Author: Nithujan Jegatheeswaran
# Brief: Contains all the configuration variables for the application
# Version: 16.03.2022

import random
import string

# Generate a random key for session
SECRET_KEY = ''.join([random.choice(string.printable) for _ in range(24)])

# Suppress error message due to future disabling
SQLALCHEMY_TRACK_MODIFICATIONS = False

# MySQL config
# ---
# To display the interaction with the database and the program in the console
SQLALCHEMY_ECHO = True

# Specify the rdbms, the db connector used by python, the credentials and the
SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://employee:Pa$$w0rd@localhost/db_employees'
