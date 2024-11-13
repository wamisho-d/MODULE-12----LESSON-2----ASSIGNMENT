# Task 1: Setting Up the Flask Environment and Database Connection
from flask import Flask
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="your_database"
)

cursor = db.cursor(dictionary=True)

# Task 2: Implementing CRUD Operations for Members
from flask import Flask, request, jsonify

app = Flask(__name__)

# Assuming db and cursor are already defined as shown above

@app.route('/members', methods=['POST'])
def add_member():
    data = request.get_json()
    query = "INSERT INTO Members (name, email) VALUES (%s, %s)"
    values = (data['name'], data['email'])
    try:
        cursor.execute(query, values)
        db.commit()
        return jsonify({"message": "Member added successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/members/<int:id>', methods=['GET'])
def get_member(id):
    query = "SELECT * FROM Members WHERE id = %s"
    cursor.execute(query, (id,))
    member = cursor.fetchone()
    if member:
        return jsonify(member), 200
    else:
        return jsonify({"message": "Member not found"}), 404

@app.route('/members/<int:id>', methods=['PUT'])
def update_member(id):
    data = request.get_json()
    query = "UPDATE Members SET name = %s, email = %s WHERE id = %s"
    values = (data['name'], data['email'], id)
    try:
        cursor.execute(query, values)
        db.commit()
        return jsonify({"message": "Member updated successfully!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/members/<int:id>', methods=['DELETE'])
def delete_member(id):
    query = "DELETE FROM Members WHERE id = %s"
    try:
        cursor.execute(query, (id,))
        db.commit()
        return jsonify({"message": "Member deleted successfully!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Task 3: Managing Workout Sessions

@app.route('/workouts', methods=['POST'])
def schedule_workout():
    data = request.get_json()
    query = "INSERT INTO WorkoutSessions (member_id, session_date, details) VALUES (%s, %s, %s)"
    values = (data['member_id'], data['session_date'], data['details'])
    try:
        cursor.execute(query, values)
        db.commit()
        return jsonify({"message": "Workout session scheduled successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/workouts/<int:member_id>', methods=['GET'])
def get_workouts_for_member(member_id):
    query = "SELECT * FROM WorkoutSessions WHERE member_id = %s"
    cursor.execute(query, (member_id,))
    sessions = cursor.fetchall()
    return jsonify(sessions), 200