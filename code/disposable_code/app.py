from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Pa$$w0rd@localhost/snows'
db.create_all(app)


@app.route('/')
def get_data():
    db
    return render_template('db_test.html', )
