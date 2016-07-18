import os

from flask import Flask, g

app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'database/app.sqlite'),
    SECRET_KEY='development key'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

from app.view import home_views, order_views, product_views
