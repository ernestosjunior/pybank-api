from flask import Flask
from ext.config import Config
from ext.database import db
from ext.migrate import migrate

app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)
migrate.init_app(app,db)

from models import *