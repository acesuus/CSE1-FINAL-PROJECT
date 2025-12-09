from flask import Blueprint, request, jsonify
from db import mysql
from utils.format import response_converter
from utils.auth import token_required

gms_bp = Blueprint("grandmasters", __name__)


@gms_bp.route("/", methods=["POST"])
@token_required
def create_gm():
    data = request.json
    name = data.get("name")
    rating = data.get("rating")

    if not name or rating is None:
        return jsonify({"error": "Missing fields"}), 400

    if not isinstance(name, str) or not isinstance(rating, (int, float)):
        return jsonify({"error": "Invalid data types"}), 400

    if isinstance(rating, (int, float)) and rating < 0:
        return jsonify({"error": "Rating must be positive"}), 400

    try:
        cursor = mysql.connection.cursor()
        query = "INSERT INTO grandmasters (name, rating) VALUES (%s, %s)"
        cursor.execute(query, (name, rating))
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
        cursor = mysql.connection.cursor()

        if search:
            query = "SELECT * FROM grandmasters WHERE name LIKE %s"
            cursor.execute(query, ("%" + search + "%",))
        else:
            cursor.execute("SELECT * FROM grandmasters")

        rows = cursor.fetchall()
        cursor.close()

        data = []
        for row in rows:
            data.append({"id": row[0], "name": row[1], "rating": row[2]})

        return response_converter({"grandmasters": data}, fmt), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@gms_bp.route("/<int:id>", methods=["GET"])
def get_gm(id):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM grandmasters WHERE id=%s", (id,))
        row = cursor.fetchone()
        cursor.close()

        if not row:
            return jsonify({"error": "GM not found"}), 404

        return jsonify({"gm": {"id": row[0], "name": row[1], "rating": row[2]}}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@gms_bp.route("/<int:id>", methods=["PUT"])
@token_required
def update_gm(id):
    data = request.json
    name = data.get("name")
    rating = data.get("rating")

    if not name or rating is None:
        return jsonify({"error": "Missing fields"}), 400

    if not isinstance(name, str) or not isinstance(rating, (int, float)):
        return jsonify({"error": "Invalid data types"}), 400

    if isinstance(rating, (int, float)) and rating < 0:
        return jsonify({"error": "Rating must be positive"}), 400

    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM grandmasters WHERE id=%s", (id,))
        if not cursor.fetchone():
            cursor.close()
            return jsonify({"error": "GM not found"}), 404

        query = "UPDATE grandmasters SET name=%s, rating=%s WHERE id=%s"
        cursor.execute(query, (name, rating, id))
        mysql.connection.commit()
        cursor.close()
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    return jsonify({"message": "GM updated"}), 200


@gms_bp.route("/<int:id>", methods=["DELETE"])
@token_required
def delete_gm(id):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM grandmasters WHERE id=%s", (id,))
        if not cursor.fetchone():
            cursor.close()
            return jsonify({"error": "GM not found"}), 404

        cursor.execute("DELETE FROM grandmasters WHERE id=%s", (id,))
        mysql.connection.commit()
        cursor.close()
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    return jsonify({"message": "GM deleted"}), 200
