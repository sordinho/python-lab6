# Created by Davide Sordi in 23/04/2018 at 16.46

import pymysql


def read_from_db():
	"""
	Reading task list from a DB
	:return: a dictionary of tasks { id : task}
	"""
	# prepare the query for reading from DB
	query = "SELECT * FROM tasks"

	# connection to database
	connection = pymysql.connect(user="root", password="sysadmin", host="localhost", database="todolist")

	# get a cursor
	cursor = connection.cursor()

	# execute query
	cursor.execute(query)

	# fetch result from query
	results = cursor.fetchall()

	# close cursor and connection
	cursor.close()
	connection.close()

	task_list = list()
	for result in results:
		tmp = {'id': result[0], 'description': result[1], 'urgent': result[2]}
		task_list.append(tmp)

	return task_list


def remove_from_db(id_task_to_rem):
	"""
	function for deleting task from DB
	:param task: task to delete in DB
	"""
	# delete query
	query = "DELETE FROM tasks WHERE id_task=(%s)"

	# connection to database
	connection = pymysql.connect(user="root", password="sysadmin", host="localhost", database="todolist")
	# get a cursor
	cursor = connection.cursor()

	# execute query
	cursor.execute(query, (id_task_to_rem,))
	# commit on DB
	connection.commit()
	# close cursor and connection
	cursor.close()
	connection.close()


def insert_in_db(descr, urg):
	"""
	insert a new task in DB
	:param task: the task to insert
	"""
	# insert query
	query = "INSERT INTO tasks (description,urgent) VALUES (%s,%s)"
	# connection to database
	connection = pymysql.connect(user="root", password="sysadmin", host="localhost", database="todolist")
	# get a cursor
	cursor = connection.cursor()
	# execute query
	cursor.execute(query, (descr, urg))
	# commit on DB
	connection.commit()

	query = "SELECT * FROM tasks WHERE description=(%s)"
	cursor = connection.cursor()
	cursor.execute(query, (descr,))
	connection.commit()

	result = cursor.fetchone()
	# close cursor and connection
	cursor.close()
	connection.close()
	tmp = {'id': result[0], 'description': result[1], 'urgent': result[2]}
	return tmp


def update_in_db(id, description):
	# insert query
	query = "UPDATE tasks SET description=(%s) WHERE id_task=(%s)"
	# connection to database
	connection = pymysql.connect(user="root", password="sysadmin", host="localhost", database="todolist")
	# get a cursor
	cursor = connection.cursor()
	# execute query
	cursor.execute(query, (description, id))
	# commit on DB
	connection.commit()
	cursor.close()
	connection.close()


print(read_from_db())
