from flask import Flask, redirect, url_for, request, render_template, session

app = Flask(__name__)
app.config.from_object('config')


@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html')


@app.route('/table/')
def table():
    return render_template('table.html')


@app.route('/hello/<name>')
def hello_name(name):
    # Helps in handling data in URL
    return 'Hello %s!' % name


@app.route('/admin')
def hello_admin():
    return 'Hello Admin'


@app.route('/guest/<guest>')
def hello_guest(guest):
    return 'Hello %s as Guest' % guest


@app.route('/user/<name>')
def hello_user(name):
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest', guest=name))


@app.route('/success/<name>')
def success(name):
    session['username'] = name
    return render_template('main_menu.html', username=name)


@app.route('/login/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    else:
        # for the GET method
        user = request.args.get('nm')
        return redirect(url_for('success', name=user))


@app.route('/logout')
def logout():
    username = session['username']
    session.pop('username')
    return render_template('logout.html', username=username)

# Note: application started in run.py
# if __name__ == '__main__':
#     app.run(debug=True)
