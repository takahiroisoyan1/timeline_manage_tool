from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)
# データを格納する仮のデータベース
tasks = []

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def add_task():
    new_task = request.json
    tasks.append(new_task)
    return jsonify(new_task), 201

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({'error': 'タスクが見つかりません'}), 404

    data = request.json
    task.status = data.get('status', task.status)
    db.session.commit()

    return jsonify({
        'task_id': task.task_id,
        'company_name': task.company_name,
        'deadline': task.deadline,
        'status': task.status
    })

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return '', 204



if __name__ == '__main__':
    app.run(debug=True)
