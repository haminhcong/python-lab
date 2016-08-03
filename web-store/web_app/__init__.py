import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'database/app.sqlite'),
    SECRET_KEY='development key',
    SQLALCHEMY_DATABASE_URI='sqlite:///' + os.path.join(app.root_path, 'database/app.sqlite'),
    SQLALCHEMY_TRACK_MODIFICATIONS=True
))
db = SQLAlchemy(app)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)
from web_app.views import home_views,account_views,product_views
