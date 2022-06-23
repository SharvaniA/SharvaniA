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

serverPort = 6565
serverSocket = socket(AF_INET, SOCK_STREAM)
# serverSocket.bind(("192.168.0.104", serverPort))
serverSocket.bind(('localhost', serverPort))
serverSocket.listen()
print('Server is Listening for incoming Client Requests!!!')

connectionsCounter = 0

(connectionSocket, clientAddress) = serverSocket.accept()
print("Connected with: Ip address", clientAddress)
    # connectionsCounter = connectionsCounter + 1
    # print("Accepted {} connections so far".format(connectionsCounter))
while True:
    print(connectionSocket.recv(1024))
    connectionSocket.sendall(str.encode(input()))
    # Thread(target=on_new_client, args=(connectionSocket, clientAddress)).start()
    # Thread(target=send, args=(connectionSocket, clientAddress)).start()
    # print(connectionSocket.recv(1024))
    # connectionSocket.sendall(str.encode(input("To client: ")))

# threading.Thread(target=evenAndOddFunction.printEven).start()






































# import socket

# import cv2
# import imutils

# server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# host_name  = socket.gethostname()
# host_ip = socket.gethostbyname(host_name)
# print('HOST IP:',host_ip)
# port = 9999
# socket_address = (host_ip,port)
# server_socket.bind(socket_address)
# server_socket.listen(5)
# print("LISTENING AT:",socket_address)
# while True:
#     client_socket, addr = server_socket.accept()
#     print('GOT CONNECTION FROM:', addr)
#     if client_socket:
#         vid = cv2.VideoCapture(0)

#         while (vid.isOpened()):
#             img, frame = vid.read()
#             ret, buffer = cv2.imencode('.jpg', frame)

#             file = open("image.jpg",'br')
#             #a = pickle.dumps(frame)
#             #message = struct.pack("Q", len(a)) + a

#             client_socket.sendall(frame)

#             #cv2.imshow('TRANSMITTING VIDEO', frame)
#             key = cv2.waitKey(1) & 0xFF
#             if key == ord('q'):
#                 client_socket.close()