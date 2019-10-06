
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app.settings import Settings

app = Flask(__name__)
app.config.from_object(Settings)


db = SQLAlchemy(app)

from models import *
from view import *