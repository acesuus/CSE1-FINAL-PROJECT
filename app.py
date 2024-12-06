from flask import Flask
from db import mysql
import conn

from CRUD.gms import gms_bp

app = Flask(__name__)


app.config['MYSQL_HOST'] = conn.MYSQL_HOST
app.config['MYSQL_USER'] = conn.MYSQL_USER
app.config['MYSQL_PASSWORD'] = conn.MYSQL_PASSWORD
app.config['MYSQL_DB'] = conn.MYSQL_DB

mysql.init_app(app)


app.register_blueprint(gms_bp, url_prefix="/api/gms")

if __name__ == "__main__":
    app.run(debug=True)
