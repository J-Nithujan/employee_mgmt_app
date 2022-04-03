# Employee management application
A Python web app made using the Flask framework and a MySQL database designed to help a company's HR department to manage its employees.



## Key Features

For a standard  employee:

- A login page that checks the user inputs
- Profile page that shows all key data about the logged employee
- A form that allows an employee to clock in all the task he / she did, these tasks can be edited afterwards

For an Employees from the H.R. department:

- A table that lists all the employees still under contract
  -  These employees' data can be edited
  - An employee can also be archived, thus he / she won't appear in the list anymore
- A form made to add new a employee to the list

All the persistent data are stored in the database `db_employees`.



## Planned Features

- Generation of payslips on PDF format at the end of a month
  - After payslips have been generated the inserted tasks cannot be edited anymore
  - The employees can see and download their payslips
  - If an employee's work time is lower that the one required by his / her contract, the app sends a warning email to this employee his / her supervisor.



## Installation

### Web app

This software uses Python 3.9  with the requirements listed under `/code/emyploee_app_mgmt/requirements.txt` .

Note: some of these packages are automatically installed when you install some main libraries (e.g. Flask, Flask-SQLAlchemy) but they won't be necessarily used.  

It is assumed that you have Python 3.9 installed and youd added it to your PATH variable.

1. The project can be found under `/code/employee_mgmt_app` 

2. Download the required packages with `pip install -r requirements.txt` or uses the virtualenv at `code/employee_mgmt_app/env`

   - if you want to use the existing virtualenv environment as the project's interpreter:

     1. First you need to add it to the list of interpreters:

        <img src=".\img\dev_env\interpreter_config-1.png" style="zoom:80%;" />

        <img src=".\img\dev_env\interpreter_config-2.png" style="zoom:75%;" />

   2. Then configure the project to run using this interpreter

   <img src=".\img\dev_env\run_config.png" style="zoom:75%;" />



### Database

- Use a MySQL server such as HeidiSQL

- Create the database `db_employees` with the scripts `/data/db_tables_creation_with_drop.sql`  and populate it with `/data/updated_data.sql`

- Don't forget to change the credientials in `/code/employee_mgmt_app/config.py` , default are `employee: Pa$$w0rd`

  <img src=".\img\dev_env\sql-credentials.png" />

- The changes in the database made by the application can be seen when you compare the data of the script `/data/DataGeneration_dbforge.sql` which only contains auto-generated data.

- This is the database's structure:

  <img src=".\img\db\MLD_Employees.png" style="zoom:75%;" />



## Run

To run this project you can use PyCharm with the configuration described above or if your OS is Windows you can simply run it with  `code/employee_mgmt_app/runner.bat`  

