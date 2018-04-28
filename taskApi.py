# Created by Davide Sordi in 26/04/2018 at 10.14
"""
This is a simple API for the tasklist project with a few possible actions
a) Retrieve the list of availables tasks
b) Create a new task
c) Retrieve the task identified by the given task id
d) Update an existing task
e) Delete an existing task

structure
task = {'id':0 , 'description':"foo" , 'urgent':"0/1"}

"""

from flask import Flask, jsonify, request

import taskDB

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
	idx = int(id)  # this is the integer value of the id of one task
	# search for a task
	task = [task for task in task_list if task['id'] == idx]
	print(task, len(task))
	if len(task) == 1:
		return jsonify(task[0])
	else:
		response = jsonify({'message': 'task not found with id: ' + id})
		response.status_code = 404
		return response


# d) we can only update the description for the  moment
@app.route('/tasks/<id>', methods=["PUT"])
def updateTask(id):
	idx = int(id)  # this is the integer value of the id of one task
	description = request.json
	task = [task for task in task_list if task['id'] == idx]
	if len(task) != 1:
		response = jsonify({'message': 'task not found with id: ' + id})
		response.status_code = 404
		return response
	else:
		task[0]['description'] = description
		# print(task)
		taskDB.update_in_db(idx, description)
		return jsonify(task[0])


# e)
@app.route('/tasks/<id>', methods=["DELETE"])
def deleteTask(id):
	idx = int(id)  # this is the integer value of the id of one task
	task = [task for task in task_list if task['id'] == idx]
	print(task)
	if len(task) != 1:
		response = jsonify({'message': 'task not found with id: ' + id})
		response.status_code = 404
		return response
	else:
		task_list.remove(task[0])
		taskDB.remove_from_db(idx)
		return jsonify(task[0])


if __name__ == '__main__':
	app.run()
