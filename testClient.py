# Created by Davide Sordi in 27/04/2018 at 15.19

import requests

base_url = 'http://127.0.0.1:5000/'

if __name__ == '__main__':
	# a) get list of tasks
	task_list = requests.get(base_url + 'tasks').json()
	print(task_list)

	# b) create a new task
	new_task = {'description': "this is a new task1", 'urgent': 1}
	requests.post(base_url + 'tasks', json=new_task)

	# c) Retrieve the task identified by the given task id
	# task_id = task_list[0]['id']
	# task_info = requests.get(base_url + "tasks" + task_id)
	# print(task_info)

	# d) todo Update an existing task
	# e) todo Delete an existing task