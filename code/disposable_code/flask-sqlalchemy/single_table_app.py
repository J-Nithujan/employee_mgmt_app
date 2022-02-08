from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import *


app = Flask(__name__)
# pip install mysql-connector-python to use '+mysqlconnector'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:Pa$$w0rd@localhost/snows'
db = SQLAlchemy(app)

Users = Table('users', db.metadata, autoload_with=db.engine)
Snows = Table('snows', db.metadata, autoload_with=db.engine)


@app.route('/')
def get_data():
    stmt_users = select(Users).where(Users.columns.id == 12)
    stmt_snows = select(Snows).where(Snows.columns.qtyAvailable > 10)
    with db.engine.connect() as conn:
        for row in conn.execute(stmt_users):
            # doesn't display in the web page
            print(row)
            
    with db.engine.connect() as conn:
        for row in conn.execute(stmt_snows):
            # doesn't display in the web page
            print(row)
    return ''


if __name__ == "__main__":
    app.run(debug=True)
