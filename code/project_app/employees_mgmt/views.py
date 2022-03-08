import flask
from flask import Flask, redirect, url_for, render_template, session

app = Flask(__name__)
app.config.from_object('config')


@app.route('/')
@app.route('/login/')
def login():  # put application's code here
    if 'username' in session:
        redirect(url_for('index'))
    else:
        return render_template('login.html')
    pass


@app.route('/')
@app.route('/index/')
def index():
    if 'username' in session:
        redirect(url_for('index'))
    else:
        return render_template('index.html')
    pass


if __name__ == '__main__':
    app.run()
