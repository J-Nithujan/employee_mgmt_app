from .views import app
from .model.tables import db

# Connect sqlalchemy to the app
# Database already exists so we don't need to initialize it
db.init_app(app)
