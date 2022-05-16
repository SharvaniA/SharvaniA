# CRUDS of bank Details using CSV
import csv
fields = ['ID', 'Name', 'Balance']
fileName = 'crudsBankDetails.csv'
records = []
def loadList():
	with open(fileName, 'r') as csvFile:
		csvwriter = csv.reader(csvFile)
def saveList():
	with open(fileName, 'w', newline = '') as csvFile:
		csvwriter = csv.writer(csvFile)
		csvwriter.writerow(fields)
		csvwriter.writerows(records)
def create():
	record = []
	record.append(input("Enter Account Number: "))
	record.append(input("Enter Name: "))
	record.append(input("Enter Balance: "))
	record.append(1)
	records.append(record)
	saveList()
def display():
	index = 0
	for record in records:
		if record[3] == 1:
			print("Account Number: " + record[0])
			print("Name: " + record[1])
			print("Balance: " + record[2])
def search():
	elementToSearch = input("Enter Account Number to search: ")
	for record in records:
		if record[0] == elementToSearch:
			if record[3] == 1:
				print("Account Number: "+ record[0])
				print("Name: " + record[1])
				print("Balance: " + record[2])
				break
			else:
				print("Account Deleted")
def update():
	elementToSearch = input("Enter Account Number to search: ")
	for record in records:
		if record[0] == elementToSearch:
			if record[3] == 1:
				record[1] = input("Enter Name: ")
				record[2] = input("Enter Balance: ")
				saveList()
				break
def delete():
	elementToSearch = input("Enter Account Number to search: ")
	for record in records:
		if record[0] == elementToSearch:
			promptOption = input("Do you really want to delete?\n1. Yes.\n2. No.\n")
			if promptOption == '1':
				print("Account Number: "+ record[0])
				print("Name: " + record[1])
				print("Balance: " + record[2])
				record[3] = 0
				saveList()
				break
def Exit():
	quit()
functions = [create, display, search, update, delete, exit]
while functions != 5:
	loadList()
	functions[int(input("Select one of the options below to proceed.1. Create Customer Details.\n2. Display Customer Details.\n3. Search Customer Details.\n4. Update Customer Details.\n5. Delete Customer Details.\n6. Exit.\nChoice: "))-1]()


# https://docs.python.org/3/library/csv.html