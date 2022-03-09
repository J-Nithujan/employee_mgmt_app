from flask import Flask, redirect, url_for, render_template, session

app = Flask(__name__)
app.config.from_object('config')


@app.route('/')
@app.route('/login/')
def login():  # put application's code here
    # if 'username' in session:
    #     return redirect(url_for('index'))
    # else:
    #     return render_template('login.html')
    return check_login()


@app.route('/')
@app.route('/index/')
def index():
    if 'username' in session:
        return render_template('index.html')
    else:
        return redirect(url_for('login'))
    

if __name__ == '__main__':
    app.run()
