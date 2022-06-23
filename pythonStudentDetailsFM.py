records = []
fileName = 'studentDetails.dat'
def loadList():
	with open(fileName, 'r') as fpDetails:
		records = fpDetails.read()
def saveList():
	with open(fileName, 'w') as fpDetails:
		fpDetails.write(str(records))
def create():
	recordStatus = 1
	record = []
	record.append(input("Enter Student ID: "))
	record.append(input("Enter Student Name: "))
	record.append(input("Enter Fee Due: "))
	record.append(record)
	records.append(record)
	saveList()
def display():
	for record in records:
		if record[3] == 1:
			print("Student ID: " + record[0])
			print("Student Name: " + record[1])
			print("Student Fee Due: " + record[2])
def search():
	recordStatus = 1
	idToSearch = input("Enter ID to search: ")
	for record in records:
		if record[0] == idToSearch:
			if record[3] == 1:
				print("Student ID: " + record[0])
				print("Student Name: " + record[1])
				print("Student Fee Due: " + record[2])
			else:
				print("Account Deleted")
def update():
	idToSearch = input("Enter ID to search: ")
	for record in records:
		if record[0] == idToSearch:
			record[1] = input("Enter Student Name: ")
			record[2] = input("Enter Student Fee Due: ")
			saveList()
def delete():
	recordStatus = 0
	idToSearch = input("Enter ID to search: ")
	for record in records:
		if ID == idToSearch:
			print("The Deleted elements are:\n")
			print("Student ID: " + record[0])
			print("Student Name: " + record[1])
			print("Student Fee Due: " + record[2])
			record[3] = recordStatus
		saveList()
def exit():
	exit()
functions = [create, display, search, update, delete, exit]
while functions != 5:
	loadList()
	functions[int(input("1. Create.\n2. Display Student Details.\n3. Search Student Details.\n4. Update Student Details.\n5. Delete Student Details.\n6. Exit.\nChoice: "))-1]()

