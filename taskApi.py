# Created by Davide Sordi in 26/04/2018 at 10.14
"""
This is a simple API for the tasklist project with a few possible actions
a) Retrieve the list of availables tasks
b) Create a new task
c) Retrieve the task identified by the given task id
d) todo Update an existing task
e) todo Delete an existing task

structure
task = {'id':0 , 'description':"foo" , 'urgent':"0/1"}

"""

from flask import Flask, jsonify, Response, request
import json, taskDB

app = Flask(__name__)

task_list = taskDB.read_from_db()  # we need to read from DB this


# print(task_list)


# a)
@app.route('/tasks')
def listTasks():
	# we get first the list of tasks
	# tasks = [{'id': task['id'], 'task': task['description'], 'urgent': task['urgent']} for task in task_list]
	tasks = [{'id': task['id']} for task in task_list]
	return jsonify(tasks)


# b) { 'descritption':'foo', 'urgent':'0/1'}
@app.route('/tasks', methods=['POST'])
def createTask():
	new_task = request.json
	print(new_task)
	# for task in task_list:
	# 	if new_task['description'] == task["description"]:
	# 		response = jsonify({"message": "task already in list: " + task['description']})
	# 		response.status_code = 404
	# 		return response

	inserted = taskDB.insert_in_db(new_task['description'], new_task['urgent'])
	print(inserted)
	task_list.append(inserted)
	return jsonify(inserted)


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


# d)
@app.route('/tasks/<id>', methods=["PUT"])
def updateTask(id):
	description = request.json
	task = [task for task in task_list if task['id'] == id]
	if len(task) != 1:
		response = jsonify({'message': 'task not found with id: ' + id})
		response.status_code = 404
		return response
	else:
		task['description'] = description
		taskDB.update_in_db(id, description)
		return jsonify(task)


# e)
@app.route('/tasks/<id>', methods=["DELETE"])
def deleteTask(id):
	task = [task for task in task_list if task['id'] == id]
	if len(task) != 1:
		response = jsonify({'message': 'task not found with id: ' + id})
		response.status_code = 404
		return response
	else:
		task_list.remove(task)
		taskDB.remove_from_db(id)
		return jsonify(task)


if __name__ == '__main__':
	app.run()
