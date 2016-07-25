import sqlite3
import sys,os
from web_app import app

con = None
rv = sqlite3.connect(os.path.join(app.root_path, 'database/web_app.sqlite'))
rv.row_factory = sqlite3.Row
xz = rv.execute('SELECT id FROM customer WHERE account_name ="{}"'.format('admin'))
t = (xz.fetchone())
print(t['id'])