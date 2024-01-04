#main.py
import os
from dart import create_task, login, update_task
from flask import Flask, request, jsonify
from dart import create_task, login, update_task, read_all_tasks

app = Flask(__name__)

my_secret = os.environ['DART_SECRET_KEY']

# Authentication with Dart
login(my_secret)

@app.route('/read_all_tasks', methods=['GET'])
def api_read_all_tasks():
    """
    API endpoint to read all tasks in Dart.
    """
    try:
        tasks = read_all_tasks()  # This function needs to be implemented in your Dart module
        return jsonify(tasks), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/create_task', methods=['POST'])
def api_create_task():
    """
    API endpoint to create a new task in Dart.
    """
    data = request.json
    if not data:
        return jsonify({"error": "Invalid JSON or no data provided"}), 400
    required_keys = ['title', 'priority', 'tags']
    if not all(key in data for key in required_keys):
        return jsonify({"error": "Missing data for required fields"}), 400
    try:
        new_task = create_task(data['title'], priority_int=data['priority'], tag_titles=data['tags'])
        return jsonify({"message": "Task created", "task_id": new_task.duid}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/update_task', methods=['PUT'])
def api_update_task():
    """
    API endpoint to update the status of an existing task in Dart.
    """
    data = request.json
    if not data:
        return jsonify({"error": "Invalid JSON or no data provided"}), 400
    required_keys = ['task_id', 'new_status']
    if not all(key in data for key in required_keys):
        return jsonify({"error": "Missing data for required fields"}), 400
    try:
        update_task(data['task_id'], status_title=data['new_status'])
        return jsonify({"message": "Task updated"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run() 

## main.py

