from .views import app
from .model.tables import db, Tables

# Connect sqlalchemy to the app
db.init_app(app)
