from flask import Flask, request, jsonify, render_template
from db import mysql
import conn
from utils.auth import create_token


from CRUD.gms import gms_bp

app = Flask(__name__)


app.config['MYSQL_HOST'] = conn.MYSQL_HOST
app.config['MYSQL_USER'] = conn.MYSQL_USER
app.config['MYSQL_PASSWORD'] = conn.MYSQL_PASSWORD
app.config['MYSQL_DB'] = conn.MYSQL_DB

mysql.init_app(app)


app.register_blueprint(gms_bp, url_prefix="/api/gms")




@app.route("/api/login", methods=["POST"])
def login():
    data = request.json
    if not data:
        return jsonify({"error": "Request body required"}), 400
    
    username = data.get("username")
    password = data.get("password")
    
    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 400

    if username == "admin" and password == "password123":
        token = create_token()
        return jsonify({"token": token}), 200
    
    return jsonify({"error": "Invalid credentials"}), 401


if __name__ == "__main__":
    app.run(debug=True)
