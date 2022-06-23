# Framework for CRUDS.

import validateByOTP
validateByOTP.getOTPAndValidate()
# OTP.validateOTP()
records = []
fieldNames = []
menuFileName = 'menu.cfg'
fieldFileName = 'field.cfg'
dataFileName = 'framework.dat'

# Function to load data.

def loadDataList():
    records = open(dataFileName, 'r').read()

# Function to save records.

def saveList():
    open(dataFileName, 'w').write(str(records))

# Function to read Hard Coded Menu.

def loadMenu():
    return open(menuFileName, 'r').read()

# Function to read Hard Coded Field Names.

def loadFieldNamesList():
    global fieldNames
    fieldNames = eval(open(fieldFileName, 'r').read())

loadFieldNamesList()

# Functions of CRUDS.
# ===========================

def create():
    record = []
    print("1")
    for fieldName in fieldNames[0:-1]:
        record.append(input("Enter " + fieldName + ": "))
    record.append(1)
    records.append(record)
    saveList()

def display():
    for record in records:
        counter = 0
        if record[-1] == 1:
            for fieldName in fieldNames[0:-1]:
                print(fieldName + ": " + record[counter])
                counter = counter + 1
            print("\n")

def search():
    elementToSearch = input("Enter " + fieldNames[0] + ": ")
    for record in records:
        counter = 1
        if record[0] == elementToSearch:
            if record[-1] == 1:
                for fieldName in fieldNames[1:-1]:
                    print(fieldName + ": " + record[counter])
                    counter = counter + 1
                break

def update():
    elementToSearch = input("Enter " + fieldNames[0] + ": ")
    for record in records:
        counter = 0
        if record[0] == elementToSearch:
            print("2")
            if record[-1] == 1:
                for fieldName in fieldNames[1:-1]:
                    record[counter + 1] = (input("Enter " + fieldName + ": "))
                    counter = counter + 1
                break
                saveList()

def delete():
    elementToSearch = input("Enter " + fieldNames[0] + ": ")
    for record in records:
        counter = 0
        if record[0] == elementToSearch:
            promptOption = input("Do you really want to delete?\n1. Yes.\n2. No.\nChoice: ")
            if promptOption == '1':
                print("Delete Details are:\n")
                for fieldName in fieldNames[0:-1]:
                    print(fieldName + ": " + record[counter])
                    counter = counter + 1
                record[-1] = 0
                break
                saveList()

def exit():
    quit()

functions = [create, display, search, update, delete, exit]
menulines = []

# Function to Display Menu.

while functions != 5:
    loadDataList()
    functions[int(input(loadMenu()))-1]()