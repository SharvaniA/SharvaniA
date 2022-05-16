# Bank Customer Details CRUDS by List in Dictionary.

records = {}
filename = 'bankCustomerDetails.txt'
def loadList():
	global records
	with open(filename, 'r') as fpDetails:
		records = eval(fpDetails.read())
def saveList():
	with open(filename, 'w') as fpDetails:
		fpDetails.write(str(records))
def create():
	record = []
	id = input("Enter Account Number: ")
	record.append(input("Enter Name: "))
	record.append(input("Enter Balance: "))
	record.append(1)
	records[id] =  record
	saveList()
def display():
	for key, value in records.items():
		if value[2] == 1:
			print("Acount Number: " + key)
			print("Name: ", value[0])
			print("Balance: ", value[1])
def search():
	elementToSearch = input("Enter Account Number to search: ")
	for key, value in records.items():
		if key == elementToSearch:
			if value[2] == 1:
				print("Name: ", value[0])
				print("Balance: ", value[1])
				break
def update():
	elementToSearch = input("Enter Account Number to search: ")
	for key, value in records.items():
		if key == elementToSearch:
			if value[2] == 1:
				value[0] = input("Enter Name: ")
				value[1] = input("Enter Balance: ")
				saveList()
				break
def delete():
	elementToSearch = input("Enter Account Number to search: ")
	for key, value in records.items():
		if key == elementToSearch:
			promptOption = input("Do you really want to delete?\n1. Yes.\n2. No.\nChoice: ")
			if promptOption == "1":
				value[2] = 0
				saveList()
				break
def exit():
	quit()
functions = [create, display, search, update, delete, exit]
loadList()
while functions != 6:
	functions[int(input("Select the option below.\n1. Create.\n2. Display.\n3. Search.\n4. Update.\n5. Delete.\n6. Exit.\nChoice: "))-1]()

