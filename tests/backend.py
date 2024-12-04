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
    task = next((task for task in tasks if task.get('task_id') == task_id), None)
    if not task:
        return jsonify({'error': 'タスクが見つかりません'}), 404

    data = request.json
    task['company_name'] = data.get('company_name', task['company_name'])
    task['deadline'] = data.get('deadline', task['deadline'])
    task['status'] = data.get('status', task['status'])  # 状態も更新
    return jsonify(task)

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['task_id'] != task_id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
