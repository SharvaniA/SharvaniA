# Client2 program. 

from socket import *
serverName = '165.22.14.77'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
while True:
	messagetoserver = input('Enter Message for Server: ')
	bytes = str.encode(messagetoserver)
	clientSocket.sendall(bytes)
	replyfromserver = clientSocket.recv(1024)
	print('Reply Message from Server: ', replyfromserver)
	clientSocket.close()
	