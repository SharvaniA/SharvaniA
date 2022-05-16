records = []
fileName = 'employeeDetails.dat'
def loadList():
	with open(fileName, 'r') as fpDetails:
		records = fpDetails.read()
def saveList():
	with open(fileName, 'w') as fpDetails:
		fpDetails.write(str(records))
def create():
	recordStatus = 1
	record = []
	record.append(input("Enter Employee ID: "))
	record.append(input("Enter Employee Name: "))
	record.append(input("Enter Employee Salary: "))
	record.append(record)
	records.append(record)
	saveList()
def display():
	for record in records:
		if record[3] == 1:
			print("Employee ID: " + record[0])
			print("Employee Name: " + record[1])
			print("Employee Salary: " + record[2])
def search():
	recordStatus = 1
	idToSearch = input("Enter ID to search: ")
	for record in records:
		if record[0] == idToSearch:
			if record[3] == 1:
				print("Employee ID: " + record[0])
				print("Employee Name: " + record[1])
				print("Employee Salary: " + record[2])
			else:
				print("Account Deleted")
def update():
	idToSearch = input("Enter ID to search: ")
	for record in records:
		if record[0] == idToSearch:
			record[1] = input("Enter Employee Name: ")
			record[2] = input("Enter Employee Salary: ")
			saveList()
def delete():
	recordStatus = 0
	idToSearch = input("Enter ID to search: ")
	for record in records:
		if record[0] == idToSearch:
			print("The Deleted elements are:\n")
			print("Employee ID: " + record[0])
			print("Employee Name: " + record[1])
			print("Employee Salary: " + record[2])
			record[3] = recordStatus
		saveList()
def exit():
	exit()
functions = [create, display, search, update, delete, exit]
while functions != 5:
	loadList()
	functions[int(input("1. Create.\n2. Display Employee Details.\n3. Search Employee Details.\n4. Update Employee Details.\n5. Delete Employee Details.\n6. Exit.\nChoice: "))-1]()