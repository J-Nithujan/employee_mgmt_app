import os
import random
import string

# All configuration variables

# Generate a random key for session
SECRET_KEY = ''.join([random.choice(string.printable) for _ in range(24)])

# Suppress error message due to future disabling
SQLALCHEMY_TRACK_MODIFICATIONS = False

# mysql config
SQLALCHEMY_ECHO = True
SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://hr_employee:Pa$$w0rd@localhost/db_employees'
