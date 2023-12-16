from flask import Flask
from .ext import db, migrate, jwt
from .config import Config

app = Flask(__name__)

app.config.from_object(Config)

jwt.init_app(app)

db.init_app(app)
migrate.init_app(app, db)

from app.models import *
from app.routes import *
