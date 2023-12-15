from flask import Flask
from app.ext import Config, db, migrate

app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)
migrate.init_app(app, db)

from app import models
from app import routes
