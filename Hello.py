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
	records.append(record)
	saveList()
def display():
	for record in records:
		print("Account Number: " + record[0])
		print("Name: " + record[1])
		print("Balance: " + record[2])
def search():
	elementToSearch = input("Enter Account Number to search: ")
	for record in records:
		if record[0] == elementToSearch:
			print("Account Number: "+ record[0])
			print("Name: " + record[1])
			print("Balance: " + record[2])
def update():
	elementToSearch = input("Enter Account Number to search: ")
	for record in records:
		if record[0] == elementToSearch:
			record[1] = input("Enter Name: ")
			record[2] = input("Enter Balance: ")
			saveList()
def delete():
	elementToSearch = input("Enter Account Number to search: ")
	for record in records:
		if record[0] == elementToSearch:
			print("Account Number: "+ record[0])
			print("Name: " + record[1])
			print("Balance: " + record[2])
			print("Account Closed")
		saveList()
def exit():
    exit()
functions = [create, display, search, update, delete, exit]
while functions != 2:
	loadList()
	functions[int(input("1. Create.\n2. Display.\n3. Search.\n4. Update\n5. Delete.\n6. Exit.\nChoice: "))-1]()