from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Pa$$w0rd@localhost/snows'


@app.route('/')
def get_data():
    snows = db.select('SELECT * FROM snows')
    return render_template('db_test.html', snows)


if __name__ == "__main__":
    app.run(debug=True)