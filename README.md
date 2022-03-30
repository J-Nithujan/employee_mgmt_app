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
   - ...



This software uses Python 3.9  with the following requirements:

- SQLAlchemy~=1.4.32
- Werkzeug~=2.0.3
- python-dateutil~=2.8.2
- Flask~=2.0.3



## Run

(write about run in PyCharm, bat and sh files)

