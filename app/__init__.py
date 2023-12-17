from flask import Flask
from dotenv import load_dotenv
from app.models import *
from app.routes import *
from .ext import db, migrate, jwt

app = Flask(__name__)

load_dotenv()

app.config.from_pyfile("config.py")

jwt.init_app(app)

db.init_app(app)
migrate.init_app(app, db)
