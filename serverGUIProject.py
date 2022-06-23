
# server

import socket
from threading import Thread

ipAddress = 'localhost'
portNumber = 9979
server = socket.socket()
print("socket created.")
server.bind((ipAddress, portNumber))
server.listen(3)
print("Waiting for the connections...")
clientAddresses = []
chatHistory = []
def broardCast(message):
	for clientAddress in clientAddresses:
		clientAddress.send(str.encode(message + "\n"))

def transferMessages(client):
	while True:
		message = client.recv(1024).decode()
		chatHistory.append(message)
		broardCast(message)

clientCounter = 0
while True:
	client, clientAddress = server.accept()
	clientCounter += 1
	name = client.recv(1024).decode()
	broardCast( name + " Joined The Chat Room")
	print("connected with", name, "of Ip address", clientAddress)
	print("Connected With", clientCounter, "Clients till Now.")

	for message in chatHistory:
		client.send(str.encode(message + "\n"))

	clientAddresses.append(client)
	Thread(target = transferMessages, args = (client, )).start()