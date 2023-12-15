from flask_migrate import Migrate
from ext.database import db

migrate = Migrate(db=db)