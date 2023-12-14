from flask import Flask
from ext.config import Config
from ext.database import db

app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)