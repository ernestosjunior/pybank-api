from flask import Flask
from app.ext.config import Config
from app.ext.database import db
from app.ext.migrate import migrate

app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)
migrate.init_app(app,db)

from app.models import *