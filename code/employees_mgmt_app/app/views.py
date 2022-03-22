# File: views.py
# Author: Nithujan Jegatheeswaran
# Brief: 
# Version: 19.03.2022

from flask import Flask, request, redirect, url_for, render_template, session
from .model.utils import *
import base64

app = Flask(__name__)
app.config.from_object('config')


@app.route('/')
@app.route('/login/', methods=['POST'])
def login():
    if request.method == 'POST':
        if check_login(request.form['email'], request.form['password']):
            # Successfully logged in
            session['email'] = request.form['email']
            return redirect(url_for('index'))
        else:
            # Login failed
            return render_template('login.html')
    else:
        # First visit on the login page
        return render_template('login.html')


@app.route('/logout/')
def logout():
    session.clear()
    return redirect(url_for('login'))


@app.route('/index/')
def index():
    data = get_index_data(session['email'])
    session['firstname'] = data['firstname']
    session['lastname'] = data['lastname']
    if data['department'] == 'Human Ressources':
        session['is_hr_employee'] = True
    else:
        session['is_hr_employee'] = False
    return render_template('index.html', data=data)


@app.route('/tasks_list/<email>/')
def tasks_list(email):
    tasks = get_tasks(email)
    return render_template('tasks_list.html', list=tasks)


@app.route('/new_task/')
@app.route('/new_task/', methods=['POST'])
def new_task():
    if request.method == 'POST':
        add_task(request.form, session['email'])
        return redirect(url_for('tasks_list', email=session['email']))
    else:
        return render_template('new_task.html')


@app.route('/tasks_list/', methods=['POST'])
@app.route('/tasks_list/<task_id>/')
def edit_task(task_id):
    if request.method == 'POST':
        edit_task(request.form, id)
        return redirect(url_for('tasks_list', email=session['email']))
    pass


@app.route('/payslips/')
def payslips():
    # TODO: payslips page and model functions
    pass
