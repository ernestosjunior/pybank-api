from flask_migrate import Migrate
from app.ext.database import db

migrate = Migrate(db=db)