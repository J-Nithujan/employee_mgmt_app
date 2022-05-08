# File: views.py
# Author: Nithujan Jegatheeswaran
# Brief: This file indicates the routes that are available to the Flask app
# Version: 27.03.2022

from flask import Flask, request, redirect, url_for, render_template, session

from app.model.employees_mgmt import *
from app.model.tasks_mgmt import *
from app.model.addresses_mgmt import *
from app.model.jobs_mgmt import *
from app.model.departments_mgmt import *
from app.model.forms import LoginForm, EmployeeForm

app = Flask(__name__)
app.config.from_object('config')


# class TaskForm(FlaskForm):
#     project = StringField('project', validators=[InputRequired(), validators.EqualTo('Indiquer une nom de projet')])
#     title = StringField('title', validators=[InputRequired(), validators.EqualTo('Indiquer un titre pour la tâche')])
#     since = StringField('since',
#                         validators=[InputRequired(), validators.EqualTo('Indiquer une heure et une date de début')])
#     until = StringField('until', validators=[InputRequired(), validators.EqualTo('Indiquer une nom de projet')])
#     description = StringField('description',
#                               validators=[InputRequired(), validators.EqualTo('Indiquer une nom de projet')])


@app.route('/')
@app.route('/login/', methods=['POST', 'GET'])
def login():
    """
    Displays the login page and handles the login form's submission,
    when the credentials are correct redirect to the index URL.
    
    :return: Renders the template 'login.html'
    """
    form = LoginForm()

    addresses = get_all_addresses()
    form2 = EmployeeForm()

    for addr in addresses:
        form2.address_id.choices.append((addr[0], addr[1] + ' ' + addr[2]))

    if form.validate_on_submit():
    # if request.method == 'POST':

        # if check_login(request.form['email'], request.form['password']):
        # if check_login(form.email.data, form.password.data):
        if check_login2(form):
            # Successfully logged in
            session['email'] = request.form['email']
            
            return redirect(url_for('index'))
        else:
        #     # Login failed
        #     return render_template('login.html')
        #     form.login.errors.append('Identifiants incorrects')
            return render_template('form_test.html', form=form, form2=form2)
    else:
        # First visit on the login page or error in the form (WTForms)
        # return render_template('login.html')
        return render_template('form_test.html', form=form, form2=form2)


@app.route('/logout/')
def logout():
    """
    Clear Flask's session variable and displays the login page.
    
    :return: Renders the template 'login.html'
    """
    session.clear()
    return redirect(url_for('login'))


@app.route('/index/')
def index():
    """
    Gets the index page data and displays it in the 'index.html' web page.
    
    :return: Renders the template 'index.html'
    """
    # Check if the email was previously added to the session variable,
    # useful when the web server has to be reboot for tests
    data = get_employee_data(session['email'])
    if data['department'] == 'Human Resources':
        session['is_hr_employee'] = True
    else:
        session['is_hr_employee'] = False
    return render_template('index.html', data=data, is_hr_employee=session['is_hr_employee'], email=session['email'])


@app.route('/tasks_list/<email>/')
def task_list(email):
    """
    Retrieve the logged employee's tasks list for the current month and displays it in the 'task_list.html' web page.
    
    :param email: logged employee's email address
    :return: Renders the 'task_list.html' template
    """
    tasks = get_tasks_list(email)
    return render_template('task_list.html', is_hr_employee=session['is_hr_employee'], email=session['email'],
                           list=tasks)


@app.route('/new_task/', methods=['POST', 'GET'])
def new_task():
    """
    Displays the web page used to add a new accomplished task,
    on the form's submission adds the task in the database and redirect to the tasks_list's URL.

    :return: Renders the template 'new_task.html'
    """
    if request.method == 'POST':
        msg_list = insert_task(request.form, session['email'])
        if msg_list:
            return render_template('new_task.html', is_hr_employee=session['is_hr_employee'], email=session['email'],
                                   error_list=msg_list, data=request.form)
        else:
            return redirect(url_for('task_list', email=session['email']))
    else:
        return render_template('new_task.html', is_hr_employee=session['is_hr_employee'], email=session['email'])


@app.route('/task_list/edit_task/<task_id>', methods=['POST', 'GET'])
def edit_task(task_id):
    """
    Displays the web page with the form used to modify an existing task,
    on the form's submission update the task in the database and redirect to the tasks_list's URL.

    :param task_id: Task's id in the database
    :return: Renders the template 'edit_task.html'
    """
    task: Tasks = get_selected_task(task_id)
    
    if request.method == 'POST':
        errors = update_task(request.form, int(task_id), session['email'])
        if errors:
            return render_template('edit_task.html', is_hr_employee=session['is_hr_employee'], email=session['email'],
                                   is_readonly=True, data=request.form, task_id=task_id, error_list=errors)
        else:
            return redirect(url_for('task_list', email=session['email']))
    else:
        until_time = task.until.strftime('%H:%M')
        return render_template('edit_task.html', is_hr_employee=session['is_hr_employee'], email=session['email'],
                               is_readonly=True, data=task, since_time=task.since.strftime('%H:%M'),
                               until_time=task.until.strftime('%H:%M'),
                               since_date=task.since.date(), until_date=task.until.date(), task_id=task.id)


@app.route('/employee_list/')
def employee_list():
    """
    Display a page containing a list of all active employees

    :return: Renders the template `employee_list.html`
    """
    employees: list[tuple] = get_employee_list()
    return render_template('employee_list.html', is_hr_employee=session['is_hr_employee'],
                           email=session['email'], list=employees)


# @app.route('/new_employee/')
@app.route('/new_employee/', methods=['POST', 'GET'])
def new_employee():
    """
    Renders the template with the form to add a new employee

    :return: if form validation fails renders new_employee.html with the previous inputs, otherwise redirect to the view
     employee_list
    """
    options: dict = get_select_options_for_employee_form()
    if request.method == 'POST':
        errors = add_employee(request.form)
        if errors:
            hiring_date = request.form['hiring_date']
            return render_template('new_employee.html', is_hr_employee=session['is_hr_employee'],
                                   email=session['email'], addresses=options['addresses'],
                                   supervisors=options['supervisors'], departments=options['departments'],
                                   jobs=options['jobs'], error_list=errors, data=request.form, hiring_date=hiring_date)
        else:
            return redirect(url_for('employee_list'))
    else:
        return render_template('new_employee.html', is_hr_employee=session['is_hr_employee'], email=session['email'],
                               addresses=options['addresses'], supervisors=options['supervisors'],
                               departments=options['departments'], jobs=options['jobs'])


@app.route('/employee_list/edit_employee/<employee_id>/', methods=['POST', 'GET'])
def edit_employee(employee_id):
    """
    Renders the template used to edits the values of the columns `lastname`, `road`, `phone_number`, `salary`,
    `percentage`, `address_id`, `employee_id`, `department_id`, `job_id` of an employee.

    :parameter employee_id: the id of the employee that will have it's data updated
    :return: if the form validation fails renders the template `edit_employee.html`, otherwise redirect to the views
     employee_list
    """
    options: dict = get_select_options_for_employee_form()
    if request.method == 'POST':
        errors = update_employee(request.form, int(employee_id))
        if errors:
            return render_template('edit_employee.html', is_hr_employee=session['is_hr_employee'],
                                   email=session['email'], is_readonly=True,
                                   data=request.form, employee_id=employee_id, addresses=options['addresses'],
                                   supervisors=options['supervisors'], departments=options['departments'],
                                   jobs=options['jobs'], error_list=errors)
        else:
            return redirect(url_for('employee_list', email=session['email']))
    else:
        employee: Employees = get_selected_employee(employee_id)
        return render_template('edit_employee.html', is_hr_employee=session['is_hr_employee'], email=session['email'],
                               is_readonly=True, data=employee, addresses=options['addresses'],
                               supervisors=options['supervisors'], departments=options['departments'],
                               jobs=options['jobs'], employee_id=employee_id)


@app.route('/employee_list/remove_employee/<employee_id>/')
def remove_employee(employee_id):
    """
    Remove an employee from the list of employees to display on the employee list table

    :param employee_id: the id of the employee to remove
    :return: Refresh the page by redirecting to the employee list view
    """
    archive_employee(int(employee_id))
    return redirect(url_for('employee_list'))


@app.route('/payslips/')
def payslips():
    """
    Gets the employee's payslips list in the database and displays it in the 'payslips.html' web page.

    :return: Renders the template 'payslips.html'
    """
    # TODO: complete payslips template page and model functions
    return render_template('payslips.html', is_hr_employee=session['is_hr_employee'], email=session['email'])


# Functions only used in this file
# ---------------------------------------------

def get_select_options_for_employee_form() -> dict:
    """
    Gets all the list needed to build the select options of the form used to add or update a new employee

    :return: Returns a `dict` with the lists of addresses, supervisors, departments and jobs
    """
    addresses = get_all_addresses()
    supervisors = get_all_supervisors()
    departments = get_all_departments()
    jobs = get_all_jobs()
    select_options: dict = {'addresses': addresses, 'supervisors': supervisors, 'departments': departments,
                            'jobs': jobs}
    return select_options
