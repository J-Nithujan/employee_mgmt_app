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
- python-dateutil==2.8.2
- six==1.16.0
- SQLAlchemy==1.4.32
- Werkzeug==2.1.0
- zipp==3.7.0

Note: some of these packages are automatically installed when you add some main libraries (e.g. Flask, Flask-SQLAlchemy) but they won't be necessarily used.  

It is assumed that you have Python 3.9 installed and youd added   it to your PATH variable.

1. Download the directory `/code/employee_mgmt_app` from this repository

2. Download the required packages with `pip install -r requirements.txt`

3. Configure your IDE to use the newly created virtualenv

   - The IDE used for this project was PyCharm, here are some screenshots to help you configure it :

     1. First you need to add the virtualenv you just created with the script to the list of interpreters:

        <img src="D:\FPA\Annee_2\T3\Pre-TPI\employees_mgmt_app\documentation\images\dev_env\interpreter_config-1.png" style="zoom:10'%;" />

        ![](D:\FPA\Annee_2\T3\Pre-TPI\employees_mgmt_app\documentation\images\dev_env\interpreter_config-2.png)

     2. Then configure the project to run using this interpreter
     
        ![](D:\FPA\Annee_2\T3\Pre-TPI\employees_mgmt_app\documentation\images\dev_env\run_config.png)



## Run

To run this project in a dev use the run.py in command line when your configured your environment.

