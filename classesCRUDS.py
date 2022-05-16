# Class for CRUDS

class CRUDS:
	def __init__(self):
		self.records = []
		self.filename = 'bankCustomerDetails.txt'
	# def loadList(self):
		with open(self.filename, 'r') as fpDetails:
			self.records = eval(fpDetails.read())
	def saveList(self):
		open(self.filename, 'w').write(str(self.records))
	def create(self):
		self.record = []
		self.record.append(input("Enter Account Number: "))
		self.record.append(input("Enter Name: "))
		self.record.append(input("Enter Balance: "))
		self.record.append(1)
		self.records.append(self.record)
		self.saveList()
	def display(self):
		for record in self.records:
			if record[3] == 1:
				print("Account Number: " + record[0])
				print("Name: " + record[1])
				print("Balance: " + record[2])
	def search(self):
		self.elementToSearch = input("Enter Account Number to search: ")
		for record in self.records:
			if record[0] == self.elementToSearch:
				if record[3] == 1:
					print("Account Number: "+ record[0])
					print("Name: " + record[1])
					print("Balance: " + record[2])
					break
				else:
					print("Account Deleted")
	def update(self):
		self.elementToSearch = input("Enter Account Number to search: ")
		for record in self.records:
			if record[0] == self.elementToSearch:
				if record[3] == 1:
					record[1] = input("Enter Name: ")
					record[2] = input("Enter Balance: ")
					self.saveList()
					break
	def delete(self):
		self.elementToSearch = input("Enter Account Number to search: ")
		for record in self.records:
			if record[0] == self.elementToSearch:
				promptOption = input("Do you really want to delete?\n1. Yes.\n2. No.\n")
				if promptOption == '1':
					print("Account Number: "+ record[0])
					print("Name: " + record[1])
					print("Balance: " + record[2])
					record[3] = 0
					self.saveList()
					break
	def exit(self):
	    quit()
bankCRUDS = CRUDS()