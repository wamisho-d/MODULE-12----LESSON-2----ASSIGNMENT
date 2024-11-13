from flask import Flask, request, jsonify
from models import execute_query

app = Flask(__name__)

# Route to add a new member
@app.route('/members', methods=['POST'])
def add_member():
    data = request.json
    query = "INSERT INTO Members (name, age, email) VALUES (%s, %s, %s)"
    execute_query(query, (data['name'], data['age'], data['email']))
    return jsonify({'message': 'Member added successfully'}), 201

# Route to retrieve a member by ID
@app.route('/members/<int:id>', methods=['GET'])
def get_member(id):
    query = "SELECT * FROM Members WHERE id = %s"
    member = execute_query(query, (id,))
    if member:
        return jsonify(member[0])
    return jsonify({'error': 'Member not found'}), 404

# Route to update a member
@app.route('/members/<int:id>', methods=['PUT'])
def update_member(id):
    data = request.json
    query = "UPDATE Members SET name = %s, age = %s, email = %s WHERE id = %s"
    execute_query(query, (data['name'], data['age'], data['email'], id))
    return jsonify({'message': 'Member updated successfully'})

# Route to delete a member
@app.route('/members/<int:id>', methods=['DELETE'])
def delete_member(id):
    query = "DELETE FROM Members WHERE id = %s"
    execute_query(query, (id,))
    return jsonify({'message': 'Member deleted successfully'})

# Route to schedule a new workout session
@app.route('/workouts', methods=['POST'])
def add_workout():
    data = request.json
    query = "INSERT INTO WorkoutSessions (member_id, session_date, duration) VALUES (%s, %s, %s)"
    execute_query(query, (data['member_id'], data['session_date'], data['duration']))
    return jsonify({'message': 'Workout session scheduled successfully'}), 201

# Route to update an existing workout session
@app.route('/workouts/<int:id>', methods=['PUT'])
def update_workout(id):
    data = request.json
    query = "UPDATE WorkoutSessions SET session_date = %s, duration = %s WHERE id = %s"
    execute_query(query, (data['session_date'], data['duration'], id))
    return jsonify({'message': 'Workout session updated successfully'})

# Route to retrieve all workout sessions
@app.route('/workouts', methods=['GET'])
def get_all_workouts():
    query = "SELECT * FROM WorkoutSessions"
    workouts = execute_query(query)
    return jsonify(workouts)

# Route to retrieve all workout sessions for a specific member
@app.route('/members/<int:member_id>/workouts', methods=['GET'])
def get_member_workouts(member_id):
    query = "SELECT * FROM WorkoutSessions WHERE member_id = %s"
    workouts = execute_query(query, (member_id,))
    return jsonify(workouts)

# Error handling for invalid routes
@app.errorhandler(404)
def not_found(e):
    return jsonify({'error': 'Route not found'}), 404

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
