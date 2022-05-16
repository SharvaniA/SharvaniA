# CRUDS Bank Customer Details using JSON.

import xml.etree.ElementTree as ET
records = []
fileName = "bankCustomersXML.xml"
tree = ET.parse(fileName)
root = tree.getroot()
for element in root:
	record = {}
	for subElement in element:
		record[subElement.tag] = subElement.text
	records.append(record)
def saveList():
	root = ET.Element("Main")
	for  record in records:
		element = ET.SubElement(root, "customer")
		for key, value in record.items():
			subElement = ET.SubElement(element, key)
			subElement.text = value
	tree = ET.ElementTree(root)
	with open(fileName, "wb") as fpBank:
		tree.write(fpBank)
def create():
	record = {}
	record['accountNumber'] = input("Enter Account Number: ")
	record['name'] = input("Enter Name: ")
	record['balance'] = input("Enter Balance: ")
	record['deleteStatus'] = '1'
	records.append(record)
	saveList()
def display():
	for record in records:
		for key, value in record.items():
			if record['deleteStatus'] == '1':
				if key != 'deleteStatus':
					print(key + ": " + value)
def search():
	accountNumber = input("Enter Account Number to search: ")
	for record in records:
		if record['accountNumber'] == accountNumber:
			for key, value in record.items():
				if key != "deleteStatus":
					print(key + ": " + value)
			if record['deleteStatus'] == '0':
				print("Account closed.")
			else:
				print("Account Active.")
			break
def update():
	accountNumber = input("Enter Account Number to search: ")
	for record in records:
		for key, value in record.items():
			if record['accountNumber'] == accountNumber:
				record['name'] = input("Enter Name: ")
				record['balance'] = input("Enter balance: ")
				saveList()
				break
def delete():
	accountNumber = input("Enter Account Number to search: ")
	for record in records:
		for key, value in record.items():
			if record['accountNumber'] == accountNumber:
				prompt = input("Are you sure to close the account? \n1. Yes\n2. No\nEnter your option: ")
				if prompt == '1':
					record['deleteStatus'] = '0'
					print("Account closed.")
					saveList()
				break
def exit():
	quit()
while True:
	functions = [create, display, search, update, delete, exit]
	functions[int(input("1. Create.\n2. Display.\n3. Search.\n4. Update.\n5. Delete.\n6. Exit.\nChoice: "))-1]()














# # CRUDS bank details with Index.

# import xml.etree.ElementTree as ET
# import os
# fileName = 'bankCustomersXML.xml'
# class Bank():
# 	def _init_(self):
# 		self.root = ET.Element('bankCustomersXML.xml')
# 	def saveList(self):
# 		with open(fileName, "wb") as fpBank:
# 			self.tree.write(fpBank)
# 	def loadList(self):
# 		self.tree = ET.parse(fileName)
# 		self.root = self.tree.getroot()
# 	def create(self):
# 		self.element = ET.SubElement(self.root, 'customer')
# 		self.subElement = ET.SubElement(self.element, "accountNumber")
# 		self.subElement.text = input("Enter Account Number: ")
# 		self.subElement = ET.SubElement(self.element, "Name")
# 		self.subElement.text = input("Enter Name: ")
# 		self.subElement = ET.SubElement(self.element, "balance")
# 		self.subElement.text = input("Enter Balance: ")
# 		self.subElement = ET.SubElement(self.element, "status")
# 		self.subElement.text = "1"
# 		self.tree = ET.ElementTree(self.root)
# 		self.saveList()
# 	def display(self):
# 		for element in self.root:
# 			if element[3].tag == "status" and element[3].text == "0":
# 				continue
# 			for counter in range(0, 3):
# 				print(element[counter].tag,": ", element[counter].text)
# 	def search(self):
# 		elementToSearch = input("Enter Account Number to search: ")
# 		for element in self.root:
# 			for SubElement in element:
# 				if SubElement.text == elementToSearch:
# 					for SubElement in element:
# 						if SubElement.tag != "status":
# 							print(SubElement.tag + ": " + SubElement.text)
# 	def update(self):
# 		elementToSearch = input("Enter Account Number to search: ")
# 		for element in self.root:
# 			for SubElement in element:
# 				if SubElement.text == elementToSearch:
# 					for SubElement in element:
# 						if SubElement.tag != "accountNumber":
# 							if SubElement.tag != "status":
# 								SubElement.text = input(SubElement.tag + ": ")
# 								self.saveList()
# 	def delete(self):
# 		elementToSearch = input("Enter Account Number to search: ")
# 		for element in self.root:
# 			for SubElement in element:
# 				if SubElement.text == elementToSearch:
# 					for SubElement in element:
# 						if SubElement.tag == "status":
# 							SubElement.text = "0"
# 							print("Account Closed.")
# 							self.saveList()

# 	def Exit(self):
# 		quit()
# g = Bank()
# functions = [g.create, g.display, g.search, g.update, g.delete, g.Exit]
# while functions != 5:
# 	g.loadList()
# 	functions[int(input("1.Create.\n2. Display.\n3. Search.\n4. Update.\n5. Delete.\n6. Exit.\nChoice: "))-1]()








# # CRUDS bank details using without Index.

# import xml.etree.ElementTree as ET
# import os
# fileName = 'bankCustomersXML.xml'
# class Bank():
# 	def _init_(self):
# 		self.root = ET.Element('bankCustomersXML.xml')
# 	def saveList(self):
# 		with open(fileName, "wb") as fpBank:
# 			self.tree.write(fpBank)
# 	def loadList(self):
# 		self.tree = ET.parse(fileName)
# 		self.root = self.tree.getroot()
# 	def create(self):
# 		self.element = ET.SubElement(self.root, 'customer')
# 		self.subElement = ET.SubElement(self.element, "accountNumber")
# 		self.subElement.text = input("Enter Account Number: ")
# 		self.subElement = ET.SubElement(self.element, "Name")
# 		self.subElement.text = input("Enter Name: ")
# 		self.subElement = ET.SubElement(self.element, "balance")
# 		self.subElement.text = input("Enter Balance: ")
# 		self.subElement = ET.SubElement(self.element, "status")
# 		self.subElement.text = "1"
# 		self.tree = ET.ElementTree(self.root)
# 		self.saveList()
# 	def display(self):
# 		for element in self.root:
# 			for SubElement in element:
# 				if SubElement.tag == "status" and SubElement.text == "1":
# 					for SubElement in element:
# 						if SubElement.tag != "status":
# 							print(SubElement.tag,": ", SubElement.text)

# 	def search(self):
# 		elementToSearch = input("Enter Account Number to search: ")
# 		for element in self.root:
# 			for SubElement in element:
# 				if SubElement.text == elementToSearch:
# 					for SubElement in element:
# 						if SubElement.tag != "status":
# 							print(SubElement.tag + ": " + SubElement.text)
# 	def update(self):
# 		elementToSearch = input("Enter Account Number to search: ")
# 		for element in self.root:
# 			for SubElement in element:
# 				if SubElement.text == elementToSearch:
# 					for SubElement in element:
# 						if SubElement.tag != "AccountNumber":
# 							if SubElement.tag != "status":
# 								SubElement.text = input(SubElement.tag + ": ")
# 								self.saveList()
# 	def delete(self):
# 		elementToSearch = input("Enter Account Number to search: ")
# 		for element in self.root:
# 			for SubElement in element:
# 				if SubElement.text == elementToSearch:
# 					for SubElement in element:
# 						if SubElement.tag == "status":
# 							SubElement.text = "0"
# 							print("Account Closed.")
# 							self.saveList()

# 	def exit(self):
# 		quit()
# g = Bank()
# functions = [g.create, g.display, g.search, g.update, g.delete, g.exit]
# while functions != 5:
# 	g.loadList()
# 	functions[int(input("1.Create.\n2. Display.\n3. Search.\n4. Update.\n5. Delete.\n6. Exit.\nChoice: "))-1]()























# Neglect this

# from xml.dom import minidom
# import xml.etree.ElementTree as gfg 
# import os
# from bs4 import BeautifulSoup
# fileName = 'bankCustomersXML.xml'


# class Bank():
# 	def __init__(self):
# 		self.root = gfg.Element('BankCustomer')
# 		# pass
# 	def saveList(self):
# 		with open(fileName, "wb") as fpDetails:
# 			self.tree.write(fpDetails)
# 	def loadList(self):
# 		# anyVariable = gfg.parse(fileName)
# 		with open(fileName, 'r') as fpDetails:
# 			# self.tree.read(fpDetails)
# 			self.data = fpDetails.read()
# 			# self.root = self.data.getroot()
# 			# self.root = anyVariable.getroot()
# 	# bs_data = BeautifulSoup(data, 'xml')
# 	def create(self):
# 		# root = minidom.Document()

# 		self.h1 = gfg.Element('note')
# 		self.root.append(self.h1)

# 		self.a1 = gfg.SubElement(self.h1, 'Status')
# 		self.a1.text = "1"

# 		self.a2 = gfg.SubElement(self.h1, "AccountNumber")
# 		self.a2.text = input("Enter Account Number: ")

# 		self.a3 = gfg.SubElement(self.h1, 'Name')
# 		self.a3.text = input("Enter Name: ")

# 		self.a4 = gfg.SubElement(self.h1, 'Balance')
# 		self.a4.text = input("Enter Balance: ")

# 		# root.appendChild(productChild)

# 		self.tree = gfg.ElementTree(self.root)

# 		# saveList()
# 		# with open(fileName, "ab") as fpDetails:
# 		# 	tree.write(fpDetails)
# 		self.saveList()
# 		# self.h1 = gfg.Element('note')
# 		# self.root.append(self.h1)
# 	# def display(self):
# 	# 	counter = 0
# 	# 	for element in self.root:
# 	# 		for SubElement in element:
# 	# 			if SubElement.tag != 'Status':
# 	# 				# for SubElement in element:
# 	# 				# if SubElement.text != '0':
# 	# 				# if counter == 3:
# 	# 					print(SubElement.tag + ": " + SubElement.text)
# 	# 					counter = counter + 1
# 	def display(self):
# 		for element in self.root:
# 			for SubElement in element:
# 					if SubElement.text == '0':
# 						break
# 					else:
# 						if SubElement.tag == 'Status':
# 							for SubElement in element: #		if SubElement.tag != 'Status':
# 								print(SubElement.tag + ": " + SubElement.text)
# 	def search(self):
# 		elementToSearch = input("Enter ID to search: ")
# 		for element in self.root:
# 			for SubElement in element:
# 				if SubElement.text == elementToSearch:
# 					if SubElement.tag == 'Status':
# 						if SubElement.text == '0':
# 							break
# 						else:
# 							for SubElement in element:
# 								print(SubElement.tag + ": " + SubElement.text)

# 	def update(self):
# 		elementToSearch = input("Enter ID to search: ")
# 		for element in self.root:
# 			for SubElement in element:
# 				if SubElement.text != '0':
# 					if SubElement.text == elementToSearch:
# 						for SubElement in element:
# 							if SubElement.tag != 'Status':
# 								# for SubElement in element:
# 									# if SubElement.tag != 'AccountNumber':
# 								SubElement.text = input(SubElement.tag + ": ")
# 							# print(SubElement.tag + ": " + SubElement.text)
# 								self.saveList()
# 	def delete(self):
# 		elementToSearch = input("Enter ID to search: ")
# 		for element in self.root:
# 			for SubElement in element:
# 				if SubElement.text == elementToSearch:
# 					for SubElement in element:
# 						if SubElement.tag == 'Status':
# 							SubElement.text = '0'
# 							self.saveList()
# 	def Exit(self):
# 		# with open(fileName, "ab") as fpDetails:
# 			# tree.write(fpDetails)
# 		quit()

# g = Bank()
# functions = [g.create, g.display, g.search, g.update, g.delete, g.Exit]
# while functions != 5:
# 	g.loadList()
# 	functions[int(input("1.Create.\n2. Display.\n3. Search.\n4. Update.\n5. Delete.\n6. Exit.\nChoice: "))-1]()

	
