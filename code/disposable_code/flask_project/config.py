import os
import random
import string

# In this file add all configuration variables

# Generate a random key
SECRET_KEY = ''.join([random.choice(string.printable) for _ in range(24)])

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')

# To suppress warning message
SQLALCHEMY_TRACK_MODIFICATIONS = False
