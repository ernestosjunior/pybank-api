from flask_migrate import Migrate
from .database import db

migrate = Migrate(db=db)
