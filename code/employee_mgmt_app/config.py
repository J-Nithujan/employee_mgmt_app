# File: config.py
# Author: Nithujan Jegatheeswaran
# Brief: Contains all the configuration variables for the Flask application
# Version: 27.03.2022

import os
import random
import string

# Generate a random key for session
SECRET_KEY = ''.join([random.choice(string.printable) for _ in range(24)])

# Set to True or False to suppress error message due to future disabling
SQLALCHEMY_TRACK_MODIFICATIONS = True

# To display the interaction with the database and the program in the console
SQLALCHEMY_ECHO = True

# Use the heroku postgree database uri with postgresql instead of postgres for the rdbms name
correct_db_uri = os.environ.get('DATABASE_URL').replace('postgres', 'postgresql')
SQLALCHEMY_DATABASE_URI = correct_db_uri
