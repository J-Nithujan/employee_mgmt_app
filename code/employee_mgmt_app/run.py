# File: run.py
# Author: Nithujan Jegatheeswaran
# Brief: This file can be used to run the application in a development environment
# Version: 30.03.20222

from app import app

if __name__ == '__main__':
    app.run(debug=True)
    