# Server program to forward messages from client to client.

from threading import Thread
from socket import *
addressList = []
def forwardReceviedMessages(client):
	while True:
		message = client.recv(1024).decode()
		for address in addressList:
			address.send(str.encode(message))
serverIpAdress = '192.168.0.103'
serverPort = 9927
serverSocket = socket(AF_INET,SOCK_STREAM)
print("waiting....")
serverSocket.bind((serverIpAdress, serverPort))
serverSocket.listen()
while True:
	clientSocket, clientAddress = serverSocket.accept()
	name = clientSocket.recv(1024).decode()
	# userNames.append(name)
	addressList.append(clientSocket)
	print("Connented with: ", clientAddress)
	Thread(target = forwardReceviedMessages, args = (clientSocket, )).start()



# class GUI:
# 	def __init__(self):
# 		self.userNamesWindow = TK()
# 		self.userNamesWindow.withdraw()

# 		self.userNames.title("Users")
# 		counter = 0
# 		for name in names:
# 			checkBoxVariable = IntVar()
# 			checkBox = Checkbutton(self.userNamesWindow,
# 				text = name, 
# 				variable = checkBoxVariable, 
# 				onvalue = 1,
# 				offvalue = 0, 
# 				height = 5, width = 20,
# 				command = lambda: self.goAhead()).grid(row = counter, sticky = W)
# 			counter = counter + 1
# 		self.userNamesWindow.mainloop()






# Server program to forward messages from client to client.

# from threading import Thread
# from socket import *
# addressList = []
# def forwardReceviedMessages(client):
# 	while True:
# 		message = client.recv(1024).decode()
# 		sendAll(message)
# def sendAll(message):
# 		for address in addressList:
# 			addressList.send(str.encode(message))
# serverIpAdress = '192.168.0.104'
# serverPort = 55555
# serverSocket = socket(AF_INET,SOCK_STREAM)
# print("waiting....")
# serverSocket.bind((serverIpAdress, serverPort))
# serverSocket.listen()
# while True:
# 	clientSocket, clientAddress = serverSocket.accept()
# 	addressList.append(clientSocket)
# 	print("Connented with: ", clientAddress)
# 	Thread(target = forwardReceviedMessages, args = (clientSocket,)).start()







# # Server program to forward messages from client to client.

# from threading import Thread
# from socket import *
# records = []
# # record = []
# def forwardReceviedMessages(client):
# 	while True:
# 		message = client.recv(1024).decode()
# 		sendAll(message)
# def sendAll(message):
# 		for record in records:
# 			record[0].send(str.encode(name))
# 			record[0].send(str.encode(message))
# serverIpAdress = '192.168.0.104'
# serverPort = 55555
# serverSocket = socket(AF_INET,SOCK_STREAM)
# serverSocket.bind((serverIpAdress, serverPort))
# serverSocket.listen()
# print("waiting....")
# while True:
# 	global name
# 	clientSocket, clientAddress = serverSocket.accept()
# 	clientSocket.send(str.encode("Enter your name: "))
# 	record = []
# 	record.append(clientSocket)
# 	name = clientSocket.recv(1024).decode()
# 	record.append(name)
# 	records.append(record)
# 	print("Connented with: ", clientAddress)
# 	Thread(target = forwardReceviedMessages, args = (clientSocket,)).start()


# # Server program to forward messages from client to client.

# from threading import Thread
# from socket import *
# addressList = []
# def forwardReceviedMessages(client):
# 	while True:
# 		message = client.recv(1024).decode()
# 		for address in addressList:
# 			address.send(str.encode(message))
# serverIpAdress = '192.168.0.104'
# serverPort = 9998
# serverSocket = socket(AF_INET,SOCK_STREAM)
# print("waiting....")
# serverSocket.bind((serverIpAdress, serverPort))
# serverSocket.listen()
# while True:
# 	clientSocket, clientAddress = serverSocket.accept()
# 	# clientSocket.send(str.encode("Enter your name: "))
# 	# name = clientSocket.recv(1024).decode()
# 	addressList.append(clientSocket)
# 	print("Connented with: ", clientAddress)
# 	Thread(target = forwardReceviedMessages, args = (clientSocket, )).start()