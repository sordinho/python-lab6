# Created by Davide Sordi in 27/04/2018 at 15.19

import requests

base_url = 'http://127.0.0.1:5000/'

if __name__ == '__main__':
	# a) get list of tasks
	task_list = requests.get(base_url + 'tasks').json()
	print(task_list)

	# b) create a new task
	# new_task = {'description': "this is a new task1", 'urgent': 1}
	# requests.post(base_url + 'tasks', json=new_task)

	# c) Retrieve the task identified by the given task id
	task_id = task_list[0]['id']
	task_info = requests.get(base_url + "tasks/" + str(task_id))
	print(task_info.json())

	# d) Update an existing task
	# get id of a task
	# id = task_list[0]['id']
	# id = 100
	# new_desc = "This is the new description"
	# response = requests.put(base_url + 'tasks/' + str(id), json=new_desc)
	# print(response)

	# e) Delete an existing task
	# get id of a task
	id = task_list[0]['id']
	response = requests.delete(base_url + "tasks/" + str(id))
	print(response.json())
