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
