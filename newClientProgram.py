# import socket
# from threading import Thread

# ipAddress = '165.22.14.77'
# # ipAddress = '192.168.0.101'
# portNumber = 9975
# client = socket.socket()
# client.connect((ipAddress, portNumber))
# name = input('Enter Your Name: ')
# client.send(str.encode(name))
# print(client.recv(1024).decode())
# # print(client.recv(1024).decode())
# # client.send(str.encode(input('Enter Your message: ')))
# # client.close()
# def recevice():
# 	while True:
# 		print(client.recv(1024).decode())

# def send():
# 	while True:
# 		client.send(str.encode(input("")))

# clientRecive = Thread(target = recevice).start()
# clientSent = Thread(target = send).start()

















# Client1 program. 
# Server to client program.

from threading import Thread
from socket import *
serverIPAddress = '192.168.0.104'
serverPort = 55555
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverIPAddress, serverPort))
def client1():
	while True:
		clientSocket.sendall(str.encode(input('')))
def client2():
	while True:
		print('', clientSocket.recv(1024))
Thread(target=client1).start()
Thread(target=client2).start()
		
