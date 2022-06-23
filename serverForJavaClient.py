# Python server program to send and recevice messages from client.

import jpysocket
import socket

host='localhost' #Host Name
port=12346    #Port Number
s=socket.socket() #Create Socket
s.bind((host,port)) #Bind Port And Host
s.listen(5) #Socket is Listening
print("Socket Is Listening....")
while True:
	connection,address=s.accept() #Accept the Connection
	# print("Connected To ",address)
	msgsend=jpysocket.jpyencode("") #Encript The Msg
	connection.send(msgsend) #Send Msg
	msgrecv=connection.recv(1024) #Recieve msg
	msgrecv=jpysocket.jpydecode(msgrecv) #Decript msg
	print("From Client: ",msgrecv)
	msgToClient = jpysocket.jpyencode(input("To Client:"))
	connection.send(msgToClient)
# s.close() #Close connection
# print("Connection Closed.")




















# # Server in python.
# # Connection between java client and python serveer.

# import jpysocket
# import socket

# host='localhost' #Host Name
# port=12346    #Port Number
# s=socket.socket() #Create Socket
# s.bind((host,port)) #Bind Port And Host
# s.listen(5) #Socket is Listening
# print("Socket Is Listening....")
# connection,address=s.accept() #Accept the Connection
# print("Connected To ",address)
# msgsend=jpysocket.jpyencode("Thank You For Connecting.") #Encript The Msg
# connection.send(msgsend) #Send Msg
# msgrecv=connection.recv(1024) #Recieve msg
# msgrecv=jpysocket.jpydecode(msgrecv) #Decript msg
# print("From Client: ",msgrecv)
# s.close() #Close connection
# print("Connection Closed.")