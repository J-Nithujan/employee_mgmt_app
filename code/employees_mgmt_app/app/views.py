from flask import Flask, request, redirect, url_for, render_template, session
from .model.utils import *

app = Flask(__name__)
app.config.from_object('config')


@app.route('/')
@app.route('/login/',  methods=['POST'])
def login():
    if request.method == 'POST':
        if check_login(request.form['email'], request.form['password']):
            # Successfully logged in
            session['email'] = request.form['email']
            data = get_index_data(session['email'])
            return redirect(url_for('index'))
        else:
            # Login failed
            return render_template('login.html')
    else:
        # First visit on the login page
        return render_template('login.html')
        

@app.route('/logout/')
def logout():
    session.pop('email')
    return redirect(url_for('login'))
    

@app.route('/index/')
def index():
    # if 'email' in session:
        return render_template('index.html')
    # else:
    #     return redirect(url_for('login'))
