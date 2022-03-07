import os
import random
import string

# All configuration variables

# Generate a random key
SECRET_KEY = ''.join([random.choice(string.printable) for _ in range(24)])

# TODO: add mysql connection params
# mysql config
SQLALCHEMY_ECHO = True
SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://rh_employee:Pa$$w0rd@localhost/db_employees'
