# Created by Davide Sordi in 26/04/2018 at 10.14
"""
This is a simple API for the tasklist project with a few possible actions
a) Retrieve the list of availables tasks
b) Create a new task
c) Retrieve the task identified by the given task id
d) todo Update an existing task
e) todo Delete an existing task
"""

from flask import Flask, jsonify, Response, request
import json

app = Flask(__name__)

task_list = []  # we need to read from DB this


# a)
@app.route('/tasks')
def listTasks():
	# we get first the list of tasks
	tasks = [{'task': task['description']} for task in task_list]
	return jsonify(tasks)


# b)
@app.route('/tasks', methods=['POST'])
def createTask():
	new_task = request.json \
		# todo check task is not in DB already
	task_list.append(new_task)
	# todo insert new task in DB
	return jsonify(new_task)


# c)
@app.route('/tasks/<id>')
def searchTask(id):
	# search for a task
	task = [task for task in task_list if task['id'] == id]
	if len(task) == 1:
		return jsonify(task)
	else:
		response = jsonify({'message': 'task not found with id: ' + id})
		response.status_code = 404
		return response


if __name__ == '__main__':
	app.run()
