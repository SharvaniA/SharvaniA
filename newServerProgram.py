# Server program. 
# Server to Client program.

from threading import Thread
from socket import *
def on_new_client(connectionSocket, clientAddress):
	while True:
		print(connectionSocket.recv(1024))
def send(connectionSocket, clientAddress):
	while True:
		connectionSocket.sendall(str.encode(input("" + str(clientAddress))))

serverPort = 57667
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("192.168.0.104", serverPort))
# serverSocket.bind(('localhost', serverPort))
serverSocket.listen()
print('Server is Listening for incoming Client Requests!!!')

connectionsCounter = 0
while True:
	(connectionSocket, clientAddress) = serverSocket.accept()
	print("Connected with: Ip address", clientAddress)
	connectionsCounter = connectionsCounter + 1
	print("Accepted {} connections so far".format(connectionsCounter))
	connectionSocket.sendall(str.encode("Sharvani is here."))
	Thread(target=on_new_client, args=(connectionSocket, clientAddress)).start()
	Thread(target=send, args=(connectionSocket, clientAddress)).start()
	# print(connectionSocket.recv(1024))
	# connectionSocket.sendall(str.encode(input("To client: ")))

# threading.Thread(target=evenAndOddFunction.printEven).start()































# # Server program.

# from threading import Thread
# from socket import *
# def on_new_client(connectionSocket, clientAddress):
# 	while True:
# 		print(connectionSocket.recv(1024))
# def send(connectionSocket, clientAddress):
# 	while True:
# 		connectionSocket.sendall(str.encode(input("To client: " + str(clientAddress))))

# serverPort = 55555
# serverSocket = socket(AF_INET, SOCK_STREAM)
# serverSocket.bind(('192.168.0.104', serverPort))
# serverSocket.listen()
# print('Server is Listening for incoming Client Requests!!!')

# connectionsCounter = 0
# while True:
# 	(connectionSocket, clientAddress) = serverSocket.accept()
# 	print("Connected with: Ip address", clientAddress)
# 	connectionsCounter = connectionsCounter + 1
# 	print("Accepted {} connections so far".format(connectionsCounter))
# 	connectionSocket.sendall(str.encode("Sharvani is here."))
# 	Thread(target=on_new_client, args=(connectionSocket, clientAddress)).start()
# 	Thread(target=send, args=(connectionSocket, clientAddress)).start()
# 	# print(connectionSocket.recv(1024))
# 	# connectionSocket.sendall(str.encode(input("To client: ")))

# # threading.Thread(target=evenAndOddFunction.printEven).start()




	