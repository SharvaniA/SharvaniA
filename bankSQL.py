 # Converting SQLite to MySQL. 

import mysql.connector as mysql
# import sqlite3
import pandas as pd
HOST = "165.22.14.77"
DATABASE = "dbSharvani"
USER = "sharvani"
PASSWORD = "pwdsharvani"

class BankDetailsSQL():
	def __init__(self):
		self.connection = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD)
		# self.connection = sqlite3.connect("bankDetailsFile.db
		self.cursor = self.connection.cursor()
	def create(self):
		customerId = input("Enter Account Number: ")
		customerName = input("Enter Name: ")
		customerBalance = input("Enter Balance: ")
		self.cursor.execute("""INSERT INTO bankDetails VALUES (%s, %s, %s, %s);""", (customerId, customerName, customerBalance, deleteStatus))
		self.connection.commit()
	def display(self):
		option = int(input("1. In Form Style and 2. Table Style: "))
		if option == 1:
			self.cursor.execute("SELECT * FROM bankDetails")
			self.data = self.cursor.fetchall()
			for values in self.data:
				print("Account Number: ", values[0])
				print("Name: ", values[1])
				print("Balance: ", values[2])
		else:
			print(pd.read_sql_query("SELECT * FROM bankDetails ", self.connection))
	def search(self):
		accountNumberToSearch = input("Enter Account Number to search: ")
		self.cursor.execute("""SELECT * FROM bankDetails WHERE customerId = (%s)""", (accountNumberToSearch, ))
		self.data = self.cursor.fetchone()
		print("accountNumber: ", self.data[0])
		print("Name: ", self.data[1])
		print("Balance: ", self.data[2])
	def update(self):
		self.cursor = self.connection.cursor()
		accountNumberToSearch = input("Enter Account Number to search: ")
		customerName = input("Enter Name: ")
		customerBalance = input("Enter Balance: ")
		self.cursor.execute('''UPDATE bankDetails SET customerName = %s, customerBalance = %s WHERE customerId = %s''', (customerName, customerBalance, accountNumberToSearch))
		self.connection.commit()
	def delete(self):
		accountNumberToSearch = input("Enter Account Number to search: ")
		try:
			self.cursor.execute('''DELETE FROM bankDetails WHERE customerId = %s''', (accountNumberToSearch, ))
			self.connection.commit()
		except Exception as err:
			# print("SELECT ErrorDescription FROM Error WHERE ErrorNumber = %s" %(err.sqlstate))
			self.cursor.execute('''SELECT ErrorDescription FROM Error WHERE ErrorNumber = %s''' %(err.sqlstate))
			deleteMessage = self.cursor.fetchall()
			for message in deleteMessage:
				for msg in message:
					print(msg)
			# print(err.errno)
			# print(err.sqlstate)
		print("Account closed")
	def Exit(self):
		self.connection.close()
		exit()
g = BankDetailsSQL()
functions = [g.create, g.display, g.search, g.update, g.delete, g.Exit]
while functions != 6:
	functions[int(input("1. Create1.\n2. Display.\n3. Search.\n4. Update\n5. Delete.\n6. Exit.\nChoice: "))-1]()
cursor.close()
connection.close()



















#  # Converting SQLite to MySQL. 

# import mysql.connector as mysql
# # import sqlite3
# import pandas as pd
# HOST = "165.22.14.77"
# DATABASE = "dbSharvani"
# USER = "sharvani"
# PASSWORD = "pwdsharvani"

# class BankDetailsSQL():
# 	def __init__(self):
# 		self.connection = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD)
# 		# self.connection = sqlite3.connect("bankDetailsFile.db")
# 		self.cursor = self.connection.cursor()
# 	def create(self):
# 		customerId = input("Enter Account Number: ")
# 		customerName = input("Enter Name: ")
# 		customerBalance = input("Enter Balance: ")
# 		deleteStatus = '1'
# 		self.cursor.execute("""INSERT INTO bankDetails VALUES (%s, %s, %s, %s);""", (customerId, customerName, customerBalance, deleteStatus))
# 		# self.cursor.execute("""INSERT INTO bankDetails VALUES (238, Satish, 768676)""")
# 		self.connection.commit()
# 	def display(self):
# 		option = int(input("1. In Form Style and 2. Table Style: "))
# 		if option == 1:
# 			self.cursor.execute("SELECT * FROM bankDetails")
# 			self.data = self.cursor.fetchall()
# 			for values in self.data:
# 				print("Account Number: ", values[0])
# 				print("Name: ", values[1])
# 				print("Balance: ", values[2])
# 		else:
# 			print(pd.read_sql_query("SELECT * FROM bankDetails ", self.connection))
# 	def search(self):
# 		accountNumberToSearch = input("Enter Account Number to search: ")
# 		self.cursor.execute("""SELECT * FROM bankDetails WHERE customerId = (%s)""", (accountNumberToSearch, ))
# 		self.data = self.cursor.fetchone()
# 		print("accountNumber: ", self.data[0])
# 		print("Name: ", self.data[1])
# 		print("Balance: ", self.data[2])
# 	def update(self):
# 		self.cursor = self.connection.cursor()
# 		accountNumberToSearch = input("Enter Account Number to search: ")
# 		customerName = input("Enter Name: ")
# 		customerBalance = input("Enter Balance: ")
# 		self.cursor.execute('''UPDATE bankDetails SET customerName = %s, customerBalance = %s WHERE customerId = %s''', (customerName, customerBalance, accountNumberToSearch))
# 		self.connection.commit()
# 	def delete(self):
# 		accountNumberToSearch = input("Enter Account Number to search: ")
# 		self.cursor.execute('''UPDATE bankDetails SET deleteStatus = '0' WHERE customerId = %s''', (accountNumberToSearch, ))
# 		self.connection.commit()
# 		print("Account closed")
# 	def Exit(self):
# 		self.connection.close()
# 		exit()
# g = BankDetailsSQL()
# functions = [g.create, g.display, g.search, g.update, g.delete, g.Exit]
# while functions != 6:
# 	functions[int(input("1. Create1.\n2. Display.\n3. Search.\n4. Update\n5. Delete.\n6. Exit.\nChoice: "))-1]()
# cursor.close()
# connection.close()











# # Classes

# import sqlite3
# import pandas as pd

# class BankDEtailsSQL():
# 	def __init__(self):
# 		self.connection = sqlite3.connect("bankDetailsFile.db")
# 		self.cursor = self.connection.cursor()
# 	def create(self):
# 		customerId = input("Enter Account Number: ")
# 		customerName = input("Enter Name: ")
# 		customerBalance = input("Enter Balance: ")
# 		deleteStatus = 1
# 		self.cursor.execute("""INSERT INTO bankDetails VALUES (?, ?, ?)""", (customerId, customerName, customerBalance))
# 		# self.cursor.execute("""INSERT INTO bankDetails VALUES (238, Satish, 768676)""")
# 		self.connection.commit()
# 	def display(self):
# 		option = int(input("1. In Form Style and 2. Table Style: "))
# 		if option == 1:
# 			self.cursor.execute("SELECT * FROM bankDetails")
# 			self.data = self.cursor.fetchall()
# 			for values in self.data:
# 				print("Account Number: ", values[0])
# 				print("Name: ", values[1])
# 				print("Balance: ", values[2])
# 		else:
# 			print(pd.read_sql_query("SELECT * FROM bankDetails ", self.connection))
# 	def search(self):
# 		accountNumberToSearch = input("Enter Account Number to search: ")
# 		self.cursor.execute("""SELECT * FROM bankDetails WHERE accountNumber = (?)""", (accountNumberToSearch, ))
# 		self.data = self.cursor.fetchone()
# 		print("accountNumber: ", self.data[0])
# 		print("Name: ", self.data[1])
# 		print("Balance: ", self.data[2])
# 	def update(self):
# 		self.cursor = connection.cursor()
# 		accountNumberToSearch = input("Enter Account Number to search: ")
# 		customerName = input("Enter Name: ")
# 		customerBalance = input("Enter Balance: ")
# 		self.cursor.execute('''UPDATE bankDetails SET Name = ?, balance = ? WHERE accountNumber = ?''', (customerName, customerBalance, customerId))
# 		self.connection.commit()
# 	def delete(self):
# 		accountNumberToSearch = input("Enter Account Number to search: ")
# 		self.cursor.execute('''UPDATE bankDetails SET deleteStatus = 0 WHERE accountNumber = ?''', (accountNumberToSearch, ))
# 		self.connection.commit()
# 		print("Account closed")
# 	def Exit(self):
# 		self.connection.close()
# 		exit()
# g = BankDEtailsSQL()
# functions = [g.create, g.display, g.search, g.update, g.delete, g.Exit]
# while functions != 6:
# 	functions[int(input("1. Create1.\n2. Display.\n3. Search.\n4. Update\n5. Delete.\n6. Exit.\nChoice: "))-1]()

# # Classes

# import sqlite3
# import pandas as pd

# class BankDEtailsSQL():
# 	def __init__(self):
# 		self.connection = sqlite3.connect("bankDetailsFile.db")
# 		self.cursor = self.connection.cursor()
# 	def create(self):
# 		customerId = input("Enter Account Number: ")
# 		customerName = input("Enter Name: ")
# 		customerBalance = input("Enter Balance: ")
# 		self.cursor.execute("""INSERT INTO bankDetails VALUES (?, ?, ?)""", (customerId, customerName, customerBalance))
# 		self.connection.commit()
# 	def display(self):
# 		option = int(input("1. In Form Style and 2. Table Style: "))
# 		if option == 1:
# 			self.cursor.execute("SELECT * FROM bankDetails")
# 			self.data = self.cursor.fetchall()
# 			for values in self.data:
# 				print("Account Number: ", values[0])
# 				print("Name: ", values[1])
# 				print("Balance: ", values[2])
# 		else:
# 			print(pd.read_sql_query("SELECT * FROM bankDetails ", self.connection))
# 	def search(self):
# 		accountNumberToSearch = input("Enter Account Number to search: ")
# 		self.cursor.execute("""SELECT * FROM bankDetails WHERE accountNumber = (?)""", (accountNumberToSearch, ))
# 		self.data = self.cursor.fetchone()
# 		print("accountNumber: ", self.data[0])
# 		print("Name: ", self.data[1])
# 		print("Balance: ", self.data[2])
# 	def update(self):
# 		self.cursor = connection.cursor()
# 		accountNumberToSearch = input("Enter Account Number to search: ")
# 		customerName = input("Enter Name: ")
# 		customerBalance = input("Enter Balance: ")
# 		self.cursor.execute('''UPDATE bankDetails SET Name = ?, balance = ? WHERE accountNumber = ?''', (customerName, customerBalance, customerId))
# 		self.connection.commit()
# 	def delete(self):
# 		accountNumberToSearch = input("Enter Account Number to search: ")
# 		cursor.execute('''DELETE FROM bankDetails WHERE accountNumber = ?''', (accountNumberToSearch, ))
# 		self.connection.commit()
# 		print("Account closed")
# 	def Exit(self):
# 		self.connection.close()
# 		exit()
# g = BankDEtailsSQL()
# functions = [g.create, g.display, g.search, g.update, g.delete, g.Exit]
# while functions != 6:
# 	functions[int(input("1. Create1.\n2. Display.\n3. Search.\n4. Update\n5. Delete.\n6. Exit.\nChoice: "))-1]()


# SQLite program for single domine.

# import sqlite3
# connection = sqlite3.connect("bankDetailsFile.db")
# def create():
# 	cur = connection.cursor()
# 	c_id = input("Enter Account Number: ")
# 	c_name = input("Enter Name: ")
# 	c_bal = input("Enter Balance: ")
# 	cur.execute("""INSERT INTO bankDetails VALUES (?, ?, ?)""", (c_id, c_name, c_bal))
# 	connection.commit()
# def  display():
# 	cur = connection.cursor()
# 	cur.execute("SELECT * FROM bankDetails")
# 	data = cur.fetchall()
# 	for values in data:
# 		print("Account Number: ", values[0])
# 		print("Name: ", values[1])
# 		print("Balance: ", values[2])

# def search():
# 	cur = connection.cursor()
# 	ac_no = input("Enter Account Number to search: ")
# 	cur.execute("""SELECT * FROM bankDetails WHERE accountNumber = (?)""", (ac_no, ))
# 	data = cur.fetchone()
# 	print("accountNumber: ", data[0])
# 	print("Name: ", data[1])
# 	print("balance: ", data[2])

# def update():
# 	cursor = connection.cursor()
# 	ac_no = input("Enter Account Number to search: ")
# 	c_name = input("Enter Name: ")
# 	c_bal = input("Enter Balance: ")
# 	cursor.execute('''UPDATE bankDetails SET Name = ?, balance = ? WHERE accountNumber = ?''', (c_name, c_bal, ac_no))
# 	connection.commit()
# def delete():
# 	cursor = connection.cursor()
# 	accountNumber = input("Enter Account Number to search: ")
# 	cursor.execute('''DELETE FROM bankDetails WHERE accountNumber = ?''', (accountNumber, ))
# 	connection.commit()
# 	print("Account closed")
# def Exit():
# 	connection.close()
# 	exit()
# functions = [create, display, search, update, delete, Exit]
# while functions != 6:
# 	functions[int(input("1. Create1.\n2. Display.\n3. Search.\n4. Update\n5. Delete.\n6. Exit.\nChoice: "))-1]()












# import sqlite3
# fileName = "bankSQL.db"
# connection = sqlite3.connect("fileName")
# crsr = connection.cursor()
# print("connection to the database")
# # def create():
# sql_command = """CREATE TABLE emp ( 
# employeeID INTEGER PRIMARY KEY, 
# name VARCHAR(20), 
# balance INTEGER);"""
# employeeID = []
# name = []
# balance = []
# option = int(input("Do you want to add another data?\n1. Yes.\n2. No.\nChoi"))

# while option == 1:
# 	# for i in range[:]:
# 	crsr.execute(f'INSERT INTO emp VALUES ({employeeID.append(int(input("Enter Account Number: ")))}, "{name.append((input("Enter Name: ")))}", {balance.append(int(input("Enter Balance: ")))})')
# crsr.execute("SELECT * FROM emp")
# ans = crsr.fetchall()
# for i in ans:
# 	print(i)
# 	# accountNumber.append(int(input("Enter Account Number: ")))
# 	# name.append(varchar(input("Enter Name: ")))
# 	# balance.append(int(input("Enter Balance: ")))


# crsr.execute(sql_command)
# connection.commit()
# connection.close()












# # importing module
# import sqlite3
  
# # connecting to the database
# connection = sqlite3.connect("gfg.db")
  
# # cursor
# crsr = connection.cursor()
  
# # primary key
# pk = [2, 3, 4, 5, 6]
  
# # Enter 5 students first names
# f_name = ['Nikhil', 'Nisha', 'Abhinav', 'Raju', 'Anshul']
  
# # Enter 5 students last names
# l_name = ['Aggarwal', 'Rawat', 'Tomar', 'Kumar', 'Aggarwal']
  
# # Enter their gender respectively
# gender = ['M', 'F', 'M', 'M', 'F']
  
# # Enter their jpining data respectively
# date = ['2019-08-24', '2020-01-01', '2018-05-14', '2015-02-02', '2018-05-14']
  
# for i in range(5):
  
#     # This is the q-mark style:
#     crsr.execute(f'INSERT INTO emp VALUES ({pk[i]}, "{f_name[i]}", "{l_name[i]}", "{gender[i]}", "{date[i]}")')
  
# # To save the changes in the files. Never skip this.
# # If we skip this, nothing will be saved in the database.
# connection.commit()
  
# # close the connection
# connection.close()