#!user/bin/python3
"""Apis with flask python framework"""
from flask import Flask, jsonify, abort, request, url_for, make_response
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()


@auth.get_password
def get_passwords(username):
    if username == 'luffy':
        return 'vodka'
    return None


@auth.error_handler
def unauthorized():
    # return make_response(jsonify({'error': 'Unauthorized access'})), 401
    return make_response(jsonify({'error': 'Unauthorized access'})), 403


tasks = [
    {
        'id': 1,
        'title': 'Buy groceries',
        'description': 'milk, cheese, pizza, fruit, tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': 'learn Python',
        'description': 'Need to find a good Python tutorial on the web',
        'done': False
    }
]


@app.route('/todo/api/v1.0/tasks', methods=['GET'])
@auth.login_required
def get_tasks():
    """GET method to return tasks list"""
    # return jsonify({'tasks': tasks})
    return jsonify({'tasks': [make_public_task(task) for task in tasks]})


@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    """Get method to return an specific task"""
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    # return jsonify({'task': task[0]})
    return jsonify({'tasks': make_public_task(task[0])})


@app.route('/todo/api/v1.0/tasks', methods=['POST'])
def create_task():
    if not request.json:
        abort(400)
    elif 'title' not in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    # return jsonify({'task': task}), 201
    return jsonify({'tasks': make_public_task(task)})


@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(404)
    if 'title' in request.json and type(request.json['title']) != unicode:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not unicode:
        abort(400)
    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['description'] = request.json.get('description', task[0]['description'])
    task[0]['done'] = request.json.get('done', task[0]['done'])
    # return jsonify({'task': task[0]})
    return jsonify({'tasks': make_public_task(task[0])})


@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    tasks.remove(task[0])
    return jsonify({'result': True})


def make_public_task(task):
    new_task = {}
    for field in task:
        if field == 'id':
            new_task['uri'] = url_for('get_task', task_id=task['id'],
                                      _external=True)
        else:
            new_task[field] = task[field]
    return new_task






if __name__ == "__main__":
    app.run(debug=True)
