

from socket import *
from threading import Thread
serverIPAddress = '192.168.0.104'
# serverIPAddress = '192.168.43.210'
# serverIPAddress = '165.22.14.77'
# serverPort = 2565
# serverPort = 1340
serverPort = 2727
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverIPAddress, serverPort))
def printReceviedMessage():
	while True:
		print("\n ", clientSocket.recv(1024))
def sendMessage():
	while True:
		clientSocket.sendall(str.encode(input("")))
clientRecv = Thread(target=printReceviedMessage).start()
clientSend = Thread(target=sendMessage).start()