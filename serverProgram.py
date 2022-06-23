import socket

# Create a server socket
serverSocket = socket.socket()
print("Server socket created")

# Associate the server socket with the IP and Port
ipAddress      = "192.168.0.101"
portNumber    = 35491

serverSocket.bind((ipAddress, portNumber))

print("Server socket bound with with ip {} port {}".format(ipAddress, portNumber))

# Make the server listen for incoming connections
serverSocket.listen()

# Server incoming connections "one by one"
clientConnectionCounter = 0

while(True):
    (clientConnection, clientAddress) = serverSocket.accept()
    clientConnectionCounter = clientConnectionCounter + 1
    print("Accepted {} connections so far".format(clientConnectionCounter))

    # read from client connection
    while(True):
        data = clientConnection.recv(1024)
        print(data)
        if(data!=b''):
            message1            = "Hi Client! Read everything you sent"
            message1Bytes       = str.encode(message1)           

            message2            = "Now I will close your connection"
            message2Bytes       = str.encode(message2) 

            clientConnection.send(message1Bytes)
            clientConnection.send(message2Bytes)

            print("Connection closed")
            break



# # Server program.

# from socket import *
# serverPort = 12000
# serverSocket = socket(AF_INET, SOCK_STREAM)
# serverSocket.bind(('165.22.14.77', serverPort))
# serverSocket.listen(1)
# print('Server is Listening for incoming Client Requests!!!')
# while True:
#         (connectionSocket, addr) = serverSocket.accept()
#         messagefromclient = connectionSocket.recv(1024)
#         print('Message from Client: ', messagefromclient)
#         messagefromserver = input('Enter reply message for clients: ')
#         bytes = str.encode(messagefromserver)
#         connectionSocket.sendall(bytes)
