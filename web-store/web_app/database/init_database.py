import sqlite3
from web_app import app
from flask import g
from flask_sqlalchemy import SQLAlchemy

from web_app import db
db.create_all()
