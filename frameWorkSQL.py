# Framework program on SQLite.


import mysql.connector as mysql
import sqlite3
import pandas as pd
HOST = "165.22.14.77"
DATABASE = "dbSharvani"
USER = "sharvani"
PASSWORD = "pwdsharvani"
fieldNames = []
fieldValues = []
fileName = 'frameWorkFile.db'
connection = sqlite3.connect(fileName)
cursor = connection.cursor()
data = cursor.execute('''SELECT * FROM frameWork''')
for fields in data.description:
	fieldNames.append(fields[0])

# Getting menu details from file.
def loadMenu():
	global menu
	menu = open('menu.cfg', 'r').read()

def cleanQuotes(string):
	string = "\'" + string + "\'"
	return string

# Inserting Values into Table.
def create():
	fieldValues = []
	for fields in fieldNames[:-1]:
		fieldValues.append(input("Enter " + str(fields) + ": "))
	fieldValues.append('1')
	cursor.execute('''INSERT INTO frameWork Values ''' + str(tuple(fieldValues)))
	connection.commit()

# Displaying all the details in Table formate and Form style.
def display():
	cursor.execute('''SELECT * FROM frameWork''')
	data = cursor.fetchall()
	formateChoice = input("Select display format option:\n1. Table Format\n2. Form Format\nChoice: ")
	if formateChoice == '1':
		print(pd.read_sql_query('''SELECT * FROM frameWork ''', connection))
	else:
		for value in data:
			if value[-1] == '1':
				index = 0
				for fields in fieldNames[:-1]:
					print(fields + ": " + str(value[index]))
					index = index + 1

# Searching record and displaying it.
def search():
	elementToSearch = input("Enter " + fieldNames[0] + ": ")
	try:
		cursor.execute("""SELECT * FROM frameWork WHERE """ + fieldNames[0] + ' = ?', (elementToSearch, ))
		data = cursor.fetchone()
		if data[-1] == '1':
			index = 0
			for fields in fieldNames[:-1]:
				print(fields + ": " + str(data[index]))
				index = index + 1
	except:
		print("Record not found.")

# Updating data in a record.
def update():
	elementToSearch = input("Enter " + fieldNames[0] + ": ")
	for fields in fieldNames[1:-1]:
		data = input("Enter " + fields + ": ")
		cursor.execute('''UPDATE frameWork SET ''' + fields + ''' = ? ''' + '''WHERE ''' + fieldNames[0] + ''' = ?''', (cleanQuotes(data), elementToSearch, ))
	connection.commit()
	if cursor.rowcount == 0:
		print("Record not found.")

# Changing the Delete Status of a record.
def delete():
	elementToSearch = input("Enter " + fieldNames[0] + ": ")
	prompt = input("Do you really want to delete?\n1. Yes.\n2. No.\nChoice: ")
	if prompt == '1':
		cursor.execute('''UPDATE frameWork SET ''' + fieldNames[-1] + ''' = 0 ''' + '''WHERE ''' + fieldNames[0] + ''' = ?''', (elementToSearch, ))
		connection.commit()
	if cursor.rowcount == 0:
		print("Record not found.")
	else:
		print("Record Deleted.")

# Exit
def Exit():
	quit()

loadMenu()
functions = [create, display, search, update, delete, Exit]
while True:
	functions[int(input(menu))-1]()














# # Framework program on SQLite.

# import sqlite3
# import pandas as pd
# fieldNames = []
# fieldValues = []
# fileName = 'frameWorkFile.db'
# connection = sqlite3.connect(fileName)
# cursor = connection.cursor()
# data = cursor.execute('''SELECT * FROM frameWork''')
# for fields in data.description:
# 	fieldNames.append(fields[0])

# # Getting menu details from file.
# def loadMenu():
# 	global menu
# 	menu = open('menu.cfg', 'r').read()

# def cleanQuotes(string):
# 	string = "\'" + string + "\'"
# 	return string

# # Inserting Values into Table.
# def create():
# 	fieldValues = []
# 	for fields in fieldNames[:-1]:
# 		fieldValues.append(input("Enter " + str(fields) + ": "))
# 	fieldValues.append('1')
# 	cursor.execute('''INSERT INTO frameWork Values ''' + str(tuple(fieldValues)))
# 	connection.commit()

# # Displaying all the details in Table formate and Form style.
# def display():
# 	cursor.execute('''SELECT * FROM frameWork''')
# 	data = cursor.fetchall()
# 	formateChoice = input("Select display format option:\n1. Table Format\n2. Form Format\nChoice: ")
# 	if formateChoice == '1':
# 		print(pd.read_sql_query('''SELECT * FROM frameWork ''', connection))
# 	else:
# 		for value in data:
# 			if value[-1] == '1':
# 				index = 0
# 				for fields in fieldNames[:-1]:
# 					print(fields + ": " + str(value[index]))
# 					index = index + 1

# # Searching record and displaying it.
# def search():
# 	elementToSearch = input("Enter " + fieldNames[0] + ": ")
# 	try:
# 		cursor.execute("""SELECT * FROM frameWork WHERE """ + fieldNames[0] + ' = ?', (elementToSearch, ))
# 		data = cursor.fetchone()
# 		if data[-1] == '1':
# 			index = 0
# 			for fields in fieldNames[:-1]:
# 				print(fields + ": " + str(data[index]))
# 				index = index + 1
# 	except:
# 		print("Record not found.")

# # Updating data in a record.
# def update():
# 	elementToSearch = input("Enter " + fieldNames[0] + ": ")
# 	for fields in fieldNames[1:-1]:
# 		data = input("Enter " + fields + ": ")
# 		cursor.execute('''UPDATE frameWork SET ''' + fields + ''' = ? ''' + '''WHERE ''' + fieldNames[0] + ''' = ?''', (cleanQuotes(data), elementToSearch, ))
# 	connection.commit()
# 	if cursor.rowcount == 0:
# 		print("Record not found.")

# # Changing the Delete Status of a record.
# def delete():
# 	elementToSearch = input("Enter " + fieldNames[0] + ": ")
# 	prompt = input("Do you really want to delete?\n1. Yes.\n2. No.\nChoice: ")
# 	if prompt == '1':
# 		cursor.execute('''UPDATE frameWork SET ''' + fieldNames[-1] + ''' = 0 ''' + '''WHERE ''' + fieldNames[0] + ''' = ?''', (elementToSearch, ))
# 		connection.commit()
# 	if cursor.rowcount == 0:
# 		print("Record not found.")
# 	else:
# 		print("Record Deleted.")

# # Exit
# def Exit():
# 	quit()

# loadMenu()
# functions = [create, display, search, update, delete, Exit]
# while True:
# 	functions[int(input(menu))-1]()










# # Framework program on SQLite.

# import sqlite3
# import pandas as pd
# fieldNames = []
# fieldValues = []
# fileName = 'frameWorkFile.db'
# connection = sqlite3.connect(fileName)
# cursor = connection.cursor()
# data = cursor.execute('''SELECT * FROM frameWork''')
# for fields in data.description:
# 	fieldNames.append(fields[0])

# # Getting menu details from file.
# def loadMenu():
# 	global menu
# 	menu = open('menu.cfg', 'r').read()

# # Inserting Values into Table.
# def create():
# 	fieldValues = []
# 	for fields in fieldNames[:-1]:
# 		fieldValues.append(input("Enter " + str(fields) + ": "))
# 	fieldValues.append('1')
# 	cursor.execute('''INSERT INTO frameWork Values ''' + str(tuple(fieldValues)))
# 	connection.commit()

# # Displaying all the details in Table formate and Form style.
# def display():
# 	cursor.execute('''SELECT * FROM frameWork''')
# 	data = cursor.fetchall()
# 	formateChoice = input("Select display format option:\n1. Table Format\n2. Form Format\nChoice: ")
# 	if formateChoice == '1':
# 		print(pd.read_sql_query('''SELECT * FROM frameWork ''', connection))
# 	else:
# 		for value in data:
# 			if value[-1] == '1':
# 				index = 0
# 				for fields in fieldNames[:-1]:
# 					print(fields + ": " + str(value[index]))
# 					index = index + 1

# # Searching record and displaying it.
# def search():
# 	elementToSearch = input("Enter " + fieldNames[0] + ": ")
# 	try:
# 		cursor.execute("""SELECT * FROM frameWork WHERE """ + fieldNames[0] + ' = ?', (elementToSearch, ))
# 		data = cursor.fetchone()
# 		if data[-1] == '1':
# 			index = 0
# 			for fields in fieldNames[:-1]:
# 				print(fields + ": " + str(data[index]))
# 				index = index + 1
# 	except:
# 		print("Record not found.")

# # Updating data in a record.
# def update():
# 	elementToSearch = input("Enter " + fieldNames[0] + ": ")
# 	for fields in fieldNames[1:-1]:
# 		data = input("Enter " + fields + ": ")
# 		cursor.execute('''UPDATE frameWork SET ''' + fields + ''' = ? ''' + '''WHERE ''' + fieldNames[0] + ''' = ?''', (data, elementToSearch, ))
# 	connection.commit()
# 	if cursor.rowcount == 0:
# 		print("Record not found.")

# # Changing the Delete Status of a record.
# def delete():
# 	elementToSearch = input("Enter " + fieldNames[0] + ": ")
# 	prompt = input("Do you really want to delete?\n1. Yes.\n2. No.\nChoice: ")
# 	if prompt == '1':
# 		cursor.execute('''UPDATE frameWork SET ''' + fieldNames[-1] + ''' = 0 ''' + '''WHERE ''' + fieldNames[0] + ''' = ?''', (elementToSearch, ))
# 		connection.commit()
# 	if cursor.rowcount == 0:
# 		print("Record not found.")
# 	else:
# 		print("Record Deleted.")

# # Exit
# def Exit():
# 	quit()

# loadMenu()
# functions = [create, display, search, update, delete, Exit]
# while True:
# 	functions[int(input(menu))-1]()













# FrameWork Program on SQlite.
#
# import sqlite3
# import pandas as pd

# fieldValues = []
# # connection = sqlite3.connect("studentDetailsFile.db")
# connection = sqlite3.connect("frameWorkFile.db")
# cursor = connection.cursor()
# data=cursor.execute('''SELECT * FROM frameWork''')
# fieldNames = []
# for fields in data.description:
# 	fieldNames.append(fields[0])
# print(fieldNames)
# def loadMenu():
# 	global menu
# 	with open('menu.cfg', 'r') as fpMenu:
# 		menu = fpMenu.read()
# def create():
# 	for fields in fieldNames[:-1]:
# 		fieldValues.append(input("Enter " + str(fields) + ": " ))
# 	fieldValues.append('1')
# 	cursor.execute("""INSERT INTO frameWork VALUES """ + str(tuple(fieldValues)))
# 	connection.commit()
# def display():
# 	cursor.execute("SELECT * FROM frameWork")
# 	data = cursor.fetchall()
# 	formateChoice = input("Select the option to display the output:\n1. Table Formate\n2. Form Formate\nChoice: ")
# 	if formateChoice == '1':
# 		print(pd.read_sql_query("SELECT * FROM frameWork ", connection))
# 	else:
# 		for value in data:
# 			if value[-1] == '1':
# 				index = 0
# 				for fields in fieldNames[:-1]:
# 					print((fields) + ": " + str(value[index]))
# 					index = index + 1
# def search():
# 	elementToSearch = input("Enter " + fieldNames[0] + ": ")
# 	cursor.execute("""SELECT * FROM frameWork WHERE """ + fieldNames[0] + ' = ?', (elementToSearch, ))
# 	data = cursor.fetchone()
# 	if data[-1] == '1':
# 		index = 0
# 		for fields in fieldNames[:-1]:
# 			print(fields + ": " + str(data[index]))
# 			index = index + 1
# def update():
# 	elementToSearch = input("Enter " + fieldNames[0] + ": ")
# 	for fields in fieldNames[1:-1]:
# 		data = input("Enter " + fields + ": ")
# 		cursor.execute('''UPDATE frameWork SET ''' + fields + ''' = ? ''' + '''WHERE ''' + fieldNames[0] + ''' = ?''', (data, elementToSearch, ))
# 			# print("Account Deleted")
# 	connection.commit()
# def delete():
# 	elementToSearch = input("Enter " + fieldNames[0] + ": ")
# 	cursor.execute('''UPDATE frameWork SET ''' + fieldNames[-1] + ''' = 0 ''' + '''WHERE ''' + fieldNames[0] + ''' = ?''', (elementToSearch, ))
# 	connection.commit()
# def Exit():
# 	quit()
# loadMenu()
# functions = [create, display, search, update, delete, Exit]
# while True:
# 	functions[int(input(menu))-1]()












# import sqlite3
# import pandas as pd

# fieldValues = []
# connection = sqlite3.connect("frameWorkFile.db")
# cursor = connection.cursor()
# data=cursor.execute('''SELECT * FROM frameWork''')
# fieldNames = []
# for fields in data.description:
# 	fieldNames.append(fields[0])
# print(fieldNames)
# def loadMenu():
# 	global menu
# 	with open('menu.cfg', 'r') as fpMenu:
# 		menu = fpMenu.read()
# 		# print(hello)
# loadMenu()
# def create():
# 	for fields in fieldNames:
# 		fieldValues.append(input("Enter " + str(fields) + ": " ))
# 	cursor.execute("""INSERT INTO frameWork VALUES """ + str(tuple(fieldValues)))
# 	# cursor.execute("""INSERT INTO bankDetails VALUES (238, Satish, 768676)""")
# 	# cursor.execute("""INSERT INTO frameWork VALUES (?,)""", fieldValues)
# 	connection.commit()
# def display():
# 	cursor.execute("SELECT * FROM frameWork")
# 	data = cursor.fetchall()
# 	# for values in data:
# 	print(pd.read_sql_query("SELECT * FROM frameWork ", connection))
# 	for value in data:
# 		index = 0
# 		for fields in fieldNames:
# 			print((fields) + ": " + str(value[index]))
# 			index = index + 1
# def search():
# 	elementToSearch = input("Enter " + fieldNames[0] + ": ")
# 	cursor.execute("""SELECT * FROM frameWork WHERE """ + fieldNames[0] + ' = ?', (elementToSearch, ))
# 	# cursor.execute("""SELECT * FROM frameWork WHERE""" + fieldValues[0] + """=""" + elementToSearch)
# 	data = cursor.fetchone()
# 	# for value in data:
# 	index = 0
# 	for fields in fieldNames:
# 		print(fields + ": " + str(data[index]))
# 		index = index + 1
# 	# for fields in fieldNames:
# 	# 	for fieldValue in fieldValues:
# 	# 		print(str(fields) + ": " + str(fieldValue))
# 		# break
# 			# print(pd.read_sql_query("SELECT * FROM frameWork ", connection))
# def update():
# 	elementToSearch = input("Enter " + fieldNames[0] + ": ")
# 	# data = cursor.fetchone()
# 	for fields in fieldNames[1:]:
# 		data = input("Enter " + fields + ": ")
# 		cursor.execute('''UPDATE frameWork SET ''' + fields + ''' = ? ''' + '''WHERE ''' + fieldNames[0] + ''' = ?''', (data, elementToSearch, ))
# 	# data = cursor.fetchone()
# 	connection.commit()
# # def search():
# # 	for fields in fieldNames:
# # 		elementToSearch = input("Enter " + str(fields[0]) + ": ")
# # 		for fieldValue in fieldValues:
# # 			if fieldValue[0] == 'elementToSearch':
# # 				print(fields + ": " + fieldValue)
# # create()
# # display()
# # search()
# # update()
# def delete():
# 	pass
# def Exit():
# 	quit()
# loadMenu()
# # print(menu)
# functions = [create, display, search, update, delete, Exit]
# while True:
# 	functions[int(input(menu))-1]()
