import jwt
import datetime
from flask import request, jsonify
from functools import wraps
SECRET_KEY = "secret_key_ni_kert"

def token_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if not check_token():
            return jsonify({"error": "Token required"}), 401
        return f(*args, **kwargs)
    return wrapper


def check_token():
    token = request.headers.get("Authorization")
    
    if not token:
        return False
    
    token = token.replace("Bearer ", "")
    
    try:
        jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return True
    except Exception:
        return False


def create_token():
    expiration = datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    token = jwt.encode({"exp": expiration}, SECRET_KEY, algorithm="HS256")
    return token