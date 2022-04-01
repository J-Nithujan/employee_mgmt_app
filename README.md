# Employee management application
A Python web app made using the Flask framework and a MySQL database designed to help a company's HR department to manage its employees.



## Key Features

For standard employees:

- A login page that checks the user inputs
- Profile page that shows all key data about the logged employee
- A form that allows an employee to clock in all the task he / she did, these tasks can be edited afterwards

Employees from the H.R. department:

- A table that lists all the employees still under contract
  -  These employees' data can be edited
  - An employee can also be archived, thus he / she won't appear in the list anymore
- A form made to add new employee to the list

All the persistent data are stored in the database `db_employees`.



## Planned Features

- Generation of payslips on PDF format at the end of a month
  - After payslips have been generated the inserted tasks cannot be edited anymore
  - The employees can see and download their payslips



## Installation

It is assumed that you have Python 3.9 installed and added to your PATH variable.

1. Download the directory `/code/employee_mgmt_app` from this repository
2. Launch the batch script `venv_script.bat`
3. Configure your IDE to use the newly created virtualenv
4. The IDE used for this project was PyCharm, here are some screenshots to help you configure it :
   - ![interpreter_config-1](C:\Pré-TPI\documentation\images\dev_env\interpreter_config-1.png)

![interpreter_config-2](C:\Pré-TPI\documentation\images\dev_env\interpreter_config-2.png)

This software uses Python 3.9  with the following requirements:

- click==8.1.0
- colorama==0.4.4
- Flask==2.1.0
- Flask-SQLAlchemy==2.5.1
- greenlet==1.1.2
- importlib-metadata==4.11.3
- itsdangerous==2.1.2
- Jinja2==3.1.1
- MarkupSafe==2.1.1
- mysql-connector-python==8.0.28
- protobuf==3.19.4
- python-dateutil==2.8.2
- six==1.16.0
- SQLAlchemy==1.4.32
- Werkzeug==2.1.0
- zipp==3.7.0



## Run

You can easily run it after you ran the`venv_script_win.bat` script file with runner_win.bat 



You can also use the newly created venv in PyCharm:

![pycharm_run_config](C:\Pré-TPI\documentation\images\dev_env\pycharm_run_config.png)

