from flask import Flask
from .views import app
from . import models

# Connect sqlalchemy to the app
models.db.init_app(app)


@app.cli.command()
def init_db():
    models.init_db()
    