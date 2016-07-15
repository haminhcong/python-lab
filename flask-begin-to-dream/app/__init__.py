from flask import Flask
app = Flask(__name__)
app.config.from_object('config')
from app import views
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

from app import models, views


