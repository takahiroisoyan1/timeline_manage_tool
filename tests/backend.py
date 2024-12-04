from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# タスク管理用のリスト
tasks = []
task_counter = 1  # タスクID用のカウンター

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def add_task():
    global task_counter
    new_task = request.json
    new_task['task_id'] = task_counter  # タスクIDを割り振る
    task_counter += 1
    tasks.append(new_task)
    return jsonify(new_task), 201

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    global tasks
    for task in tasks:
        if task['task_id'] == task_id:
            data = request.json
            task['status'] = data.get('status', task['status'])
            return jsonify(task)
    return jsonify({'error': 'タスクが見つかりません'}), 404

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['task_id'] != task_id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
