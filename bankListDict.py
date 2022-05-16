# Bank Customer Details using Dictionary in List.

records = []
filename = 'bankCustomerDetails1.txt'
def loadList():
	global records
	records = eval(open(filename, 'r').read())
def saveList():
	open(filename, 'w').write(str(records))
def create():
	record = {}
	record['Account Number'] = input("Enter Account Number: ")
	record['Name'] = input("Enter Name: ")
	record['Balance'] = input("Enter Balance: ")
	record['Status'] = '1'
	records.append(record)
	saveList()
def display():
	for record in records:
		for key, value in record.items():
			if record['Status'] == '1':
				if key != 'Status': 
					print(key + ": " + value)
def search():
	elementToSearch = input("Enter Account Number to search: ")
	for record in records:
		for key, value in record.items():
			if record['Status'] == '1':
				if record['Account Number'] == elementToSearch:
					if key != 'Status': 
						print(key + ": " + value)
def update():
	elementToSearch = input("Enter Account Number to search: ")
	for record in records:
		for key, value in record.items():
			if record['Account Number'] == elementToSearch:
				if record['Status'] == '1':
					if key != 'Status': 
						record['Account Number'] = elementToSearch
						record['Name'] = input("Enter Name: ")
						record['Balance'] = input("Enter Balance: ")
						saveList()
						break
def delete():
	elementToSearch = input("Enter Account Number to search: ")
	for record in records:
		for key, value in record.items():
			if record['Account Number'] == elementToSearch:
				promptOption = input("Do you really want to delete?\n1. Yes.\n2. No.\nChoice: ")
				if promptOption == "1":
					record['Status'] = 0
					saveList()
				break
def exit():
	quit()
functions = [create, display, search, update, delete, exit]
while  functions != 5:
	loadList()
	functions[int(input("Select the option below.\n1. Create.\n2. Display.\n3. Search.\n4. Update.\n5. Delete.\n6. Exit.\nChoice: "))-1]()

