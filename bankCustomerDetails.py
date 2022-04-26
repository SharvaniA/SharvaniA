records = []
filename = 'bankCustomerDetails.txt'
def loadList():
	with open(filename, 'r') as fpDetails:
		records = fpDetails.read()
def saveList():
	with open(filename, 'w') as fpDetails:
		fpDetails.write(str(records))
def create():
	record = []
	record.append(input("Enter Account Number: "))
	record.append(input("Enter Name: "))
	record.append(input("Enter Balance: "))
	record.append(1)
	records.append(record)
	saveList()
def display():
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
			record[1] = input("Enter Name: ")
			record[2] = input("Enter Balance: ")
			break
			saveList()
def delete():
	elementToSearch = input("Enter Account Number to search: ")
	for record in records:
		if record[0] == elementToSearch:
			print("Account Number: "+ record[0])
			print("Name: " + record[1])
			print("Balance: " + record[2])
			record[3] = 0
			break
		saveList()
def exit():
    exit()
functions = [create, display, search, update, delete, exit]
while functions != 2:
	loadList()
	functions[int(input("1. Create.\n2. Display.\n3. Search.\n4. Update\n5. Delete.\n6. Exit.\nChoice: "))-1]()