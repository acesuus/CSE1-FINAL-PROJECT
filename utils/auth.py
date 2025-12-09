import jwt
import datetime
from flask import request, jsonify

SECRET_KEY = "secret_key_ni_kert"

def check_token():
    token = request.headers.get("Authorization")
    
    if not token:
        return False
    
    token = token.replace("Bearer ", "")
    
    try:
        jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return True
    except:
        return False


def create_token():
    expiration = datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    token = jwt.encode({"exp": expiration}, SECRET_KEY, algorithm="HS256")
    return token