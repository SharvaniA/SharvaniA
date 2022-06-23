# Socket program to connect to google server.

import socket 
import sys

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print ("Socket successfully created")
except socket.error as err:
	print ("socket creation failed with error %s" %(err))

# default port for socket
port = 80

try:
	hostIp = socket.gethostbyname('www.google.com')
	print(hostIp)
except socket.gaierror:

# this means could not resolve the host
	print ("there was an error resolving the host")
	sys.exit()

# connecting to the server
s.connect((hostIp, port))

print ("the socket has successfully connected to google")