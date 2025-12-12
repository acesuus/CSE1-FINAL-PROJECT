from flask import Blueprint, request, jsonify
from db import mysql
from utils.format import response_format
from utils.auth import token_required
from datetime import datetime

gms_bp = Blueprint("grandmasters", __name__)

def get_cursor():
    mysql.connection.ping(reconnect=True)
    return mysql.connection.cursor()

def validate_gm_data(data):
    """Validate GM data types and values"""
    required_fields = [
        "first_name", "last_name", "country", "birth_year",
        "peak_rating", "current_rating", "title_year", "FIDE_id"
    ]
    
    if not all(field in data for field in required_fields):
        return False, "Missing required fields"
    
    if not (
        isinstance(data["first_name"], str) and
        isinstance(data["last_name"], str) and
        isinstance(data["country"], str) and
        isinstance(data["birth_year"], int) and
        isinstance(data["peak_rating"], int) and
        isinstance(data["current_rating"], int) and
        isinstance(data["title_year"], int) and
        isinstance(data["FIDE_id"], str)
    ):
        return False, "Invalid data types"
    
    if not data["first_name"].strip() or not data["last_name"].strip():
        return False, "Names cannot be empty"
    
    current_year = datetime.now().year
    if data["birth_year"] < 1800 or data["birth_year"] > current_year:
        return False, "Invalid birth year"
    
    if data["title_year"] < 1800 or data["title_year"] > current_year:
        return False, "Invalid title year"
    
    if data["peak_rating"] < 0 or data["current_rating"] < 0:
        return False, "Ratings must be positive"
    
    if data["current_rating"] > data["peak_rating"]:
        return False, "Current rating cannot exceed peak rating"
    
    return True, "Valid"

@gms_bp.route("/", methods=["POST"])
@token_required
def create_gm():
    data = request.json
    
    valid, message = validate_gm_data(data)
    if not valid:
        return jsonify({"error": message}), 400

    try:
        cursor = get_cursor()
        query = """
            INSERT INTO grandmasters
            (first_name, last_name, country, birth_year, 
             peak_rating, current_rating, title_year, FIDE_id)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
        """

        values = (
            data["first_name"], data["last_name"], data["country"],
            data["birth_year"], data["peak_rating"], data["current_rating"],
            data["title_year"], data["FIDE_id"]
        )

        cursor.execute(query, values)
        mysql.connection.commit()
        gm_id = cursor.lastrowid
        cursor.close()

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    return jsonify({"message": "GM added", "id": gm_id}), 201


@gms_bp.route("/", methods=["GET"])
def get_gms():
    search = request.args.get("search")
    fmt = request.args.get("format", "json")

    try:
        cursor = get_cursor()

        if search:
            query = """
                SELECT * FROM grandmasters
                WHERE first_name LIKE %s OR last_name LIKE %s
            """
            cursor.execute(query, (f"%{search}%", f"%{search}%"))
        else:
            cursor.execute("SELECT * FROM grandmasters")

        rows = cursor.fetchall()
        cursor.close()

        data = []
        for row in rows:
            data.append({
                "gm_id": row[0],
                "first_name": row[1],
                "last_name": row[2],
                "country": row[3],
                "birth_year": row[4],
                "peak_rating": row[5],
                "current_rating": row[6],
                "title_year": row[7],
                "FIDE_id": row[8]
            })

        return response_format({"grandmasters": data}, fmt)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@gms_bp.route("/<int:id>", methods=["GET"])
def get_gm(id):
    try:
        cursor = get_cursor()
        cursor.execute("SELECT * FROM grandmasters WHERE gm_id=%s", (id,))
        row = cursor.fetchone()
        cursor.close()

        if not row:
            return jsonify({"error": "GM not found"}), 404

        return jsonify({
            "gm": {
                "gm_id": row[0],
                "first_name": row[1],
                "last_name": row[2],
                "country": row[3],
                "birth_year": row[4],
                "peak_rating": row[5],
                "current_rating": row[6],
                "title_year": row[7],
                "FIDE_id": row[8]
            }
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@gms_bp.route("/<int:id>", methods=["PUT"])
@token_required
def update_gm(id):
    data = request.json
    
    valid, message = validate_gm_data(data)
    if not valid:
        return jsonify({"error": message}), 400

    try:
        cursor = get_cursor()
        cursor.execute("SELECT * FROM grandmasters WHERE gm_id=%s", (id,))
        if not cursor.fetchone():
            cursor.close()
            return jsonify({"error": "GM not found"}), 404

        query = """
            UPDATE grandmasters SET
            first_name=%s, last_name=%s, country=%s, birth_year=%s,
            peak_rating=%s, current_rating=%s, title_year=%s, FIDE_id=%s
            WHERE gm_id=%s
        """

        values = (
            data["first_name"], data["last_name"], data["country"],
            data["birth_year"], data["peak_rating"], data["current_rating"],
            data["title_year"], data["FIDE_id"], id
        )

        cursor.execute(query, values)
        mysql.connection.commit()
        cursor.close()

        return jsonify({"message": "GM updated"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@gms_bp.route("/<int:id>", methods=["DELETE"])
@token_required
def delete_gm(id):
    try:
        cursor = get_cursor()
        cursor.execute("SELECT * FROM grandmasters WHERE gm_id=%s", (id,))
        if not cursor.fetchone():
            cursor.close()
            return jsonify({"error": "GM not found"}), 404

        cursor.execute("DELETE FROM grandmasters WHERE gm_id=%s", (id,))
        mysql.connection.commit()
        cursor.close()

        return jsonify({"message": "GM deleted"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
