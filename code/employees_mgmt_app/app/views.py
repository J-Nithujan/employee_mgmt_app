from flask import Flask, request, redirect, url_for, render_template, session
from .model.utils import *

app = Flask(__name__)
app.config.from_object('config')


@app.route('/')
@app.route('/login/',  methods=['POST'])
def login():
    if 'username' in session:
        return redirect(url_for('index'))
    else:
        if request.method == 'POST':
            if check_login(request.form['email'], request.form['password']):
                session['username'] = request.form['email']
                return redirect(url_for('index'))
            else:
                return render_template('login.html')
        else:
            return render_template('login.html')
    pass


@app.route('/')
@app.route('/index/')
def index():
    if 'username' in session:
        return render_template('index.html')
    else:
        return redirect(url_for('login'))
