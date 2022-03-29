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
from app.model.payslips_mgmt import *

app = Flask(__name__)
app.config.from_object('config')


@app.route('/')
@app.route('/login/', methods=['POST', 'GET'])
def login():
    """
    Displays the login page and handles the login form's submission,
    when the credentials are correct redirect to the index URL.
    
    :return: Renders the 'login.html' template
    """
    if request.method == 'POST':
        if check_login(request.form['email'], request.form['password']):
            # Successfully logged in
            session['email'] = request.form['email']
            
            # TODO: the session.permanent value to test ???
            # Keeps the session variables for 31 days:
            # src: https://flask.palletsprojects.com/en/2.1.x/api/?highlight=session#flask.session
            session.permanent = True
            
            return redirect(url_for('index'))
        else:
            # Login failed
            return render_template('login.html')
    else:
        # First visit on the login page
        return render_template('login.html')


@app.route('/logout/')
def logout():
    """
    Clear Flask's session variable and displays the login page.
    
    :return: Renders the 'login.html' template
    """
    session.clear()
    return redirect(url_for('login'))


@app.route('/index/')
def index():
    """
    Gets the index page data and displays it in the 'index.html' web page.
    
    :return: Renders the 'index.html' template
    """
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


@app.route('/new_task/')
@app.route('/new_task/', methods=['POST'])
def new_task():
    """
    Displays the web page used to add a new accomplished task,
    on the form's submission adds the task in the database and redirect to the tasks_list's URL.

    :return: Renders the 'new_task.html' template
    """
    if request.method == 'POST':
        msg_list = add_task(request.form, session['email'])
        if msg_list:
            return render_template('new_task.html', is_hr_employee=session['is_hr_employee'], email=session['email'],
                                   error_list=msg_list, data=request.form)
        else:
            return redirect(url_for('task_list', email=session['email']))
    else:
        return render_template('new_task.html', is_hr_employee=session['is_hr_employee'], email=session['email'])


@app.route('/task_list/edit_task/<task_id>')
@app.route('/task_list/edit_task/<task_id>', methods=['POST'])
def edit_task(task_id):
    """
    Displays the web page with the form used to modify an existing task,
    on the form's submission update the task in the database and redirect to the tasks_list's URL.

    :param task_id: Task's id in the database
    :return: Renders the 'edit_task.html' template
    """
    if request.method == 'POST':
        errors = update_task(request.form, int(task_id), session['email'])
        if errors:
            return render_template('edit_task.html', is_hr_employee=session['is_hr_employee'], email=session['email'],
                                   is_disabled=True, data=request.form, task_id=task_id, error_list=errors)
        else:
            return redirect(url_for('task_list', email=session['email']))
    else:
        task = get_selected_task(task_id)
        return render_template('edit_task.html', is_hr_employee=session['is_hr_employee'], email=session['email'],
                               is_disabled=True, data=task, task_id=task.id)


@app.route('/payslips/')
def payslips():
    """
    Gets the employee's payslips list in the database and displays it the 'payslips.html' web page.
    
    :return: Renders the 'payslips.html' template
    """
    # TODO: finish payslips template page and model functions
    return render_template('payslips.html', is_hr_employee=session['is_hr_employee'], email=session['email'])


@app.route('/employee_list/')
def employee_list():
    employees: list[tuple] = get_employee_list()
    return render_template('employee_list.html', is_hr_employee=session['is_hr_employee'],
                           email=session['email'], list=employees)


@app.route('/new_employee/')
@app.route('/new_employee/', methods=['POST'])
def new_employee():
    if request.method == 'POST':
        errors = add_employee(request.form)
        if errors:
            options: dict = get_select_options_for_new_employee_form()
            return render_template('new_employee.html', is_hr_employee=session['is_hr_employee'],
                                   email=session['email'], addresses=options['addresses'],
                                   supervisors=options['supervisors'], departments=options['departments'],
                                   jobs=options['jobs'], error_list=errors, data=request.form)
        else:
            return redirect(url_for('employee_list'))
    else:
        options: dict = get_select_options_for_new_employee_form()
        return render_template('new_employee.html', is_hr_employee=session['is_hr_employee'], email=session['email'],
                               addresses=options['addresses'], supervisors=options['supervisors'],
                               departments=options['departments'], jobs=options['jobs'])


def get_select_options_for_new_employee_form() -> dict:
    addresses = get_all_addresses()
    supervisors = get_all_supervisors()
    departments = get_all_departments()
    jobs = get_all_jobs()
    select_options: dict = {'addresses': addresses, 'supervisors': supervisors, 'departments': departments,
                            'jobs': jobs}
    return select_options


@app.route('/employee_list/edit_employee/<employee_id>/')
def edit_employee(employee_id):
    if request.method == 'POST':
        errors = update_employee(request.form, int(employee_id))
        if errors:
            return render_template('edit_employee.html', is_hr_employee=session['is_hr_employee'],
                                   email=session['email'], is_disabled=True,
                                   data=request.form, employee_id=employee_id, error_list=errors)
        else:
            return redirect(url_for('employee_list', email=session['email']))
    else:
        employee = get_selected_employee(employee_id)
        return render_template('edit_employee.html', is_hr_employee=session['is_hr_employee'], email=session['email'],
                               data=employee, is_disabled=True, employee_id=employee_id)


@app.route('/employee_list/remove_employee/<employee_id>/')
def remove_employee(employee_id):
    pass
