from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import *

app = Flask(__name__)
# pip install mysql-connector-python to use '+mysqlconnector'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:Pa$$w0rd@localhost/cantonscitieslanguagesdb'
db = SQLAlchemy(app)

cantons = Table('cantons', db.metadata, autoload_with=db.engine)
cantons_has_languages = Table('cantons_has_languages', db.metadata, autoload_with=db.engine)
languages = Table('languages', db.metadata, autoload_with=db.engine)


@app.route('/')
def get_data():
    statement = select(cantons.c.name, languages.c.name).select_from(cantons_has_languages).join(cantons).\
        join(languages).order_by(cantons.c.name)
    str_data = ''
    with db.engine.connect() as conn:
        for row in conn.execute(statement):
            str_data += '<p>'
            for data in row:
                str_data += data + ' - '
            str_data = str_data[0:len(str_data) - 3]
            str_data += '</p>'
    return str_data


if __name__ == "__main__":
    app.run(debug=True)
