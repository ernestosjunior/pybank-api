from flask import Flask
from .ext import db, migrate, jwt
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()

app.config.from_pyfile("config.py")

jwt.init_app(app)

db.init_app(app)
migrate.init_app(app, db)

from app.models import *
from app.routes import *
