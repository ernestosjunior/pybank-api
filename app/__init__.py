from flask import Flask
from .ext import db, migrate
from .config import Config

app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)
migrate.init_app(app, db)

from app.models import *
from app.routes import *
