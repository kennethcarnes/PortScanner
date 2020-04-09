#!/bin/python

import sys
import socket
from datetime import datetime

#Define our target
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) #Translate hostname to IPv4
else:
	print("Invalid amount of arguments.")
	print("Syntax: python3 scanner.py <ip>")
	
#Add a pretty banner
print("-" * 50)
print("Scanning target "+target)
print("Time started: "+str(datetime.now()))
print("-" * 50)

#Check the status of ports for a given IP
try:
	for port in range(1,65535):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #IPv4, Socket
		socket.setdefaulttimeout(1) #Attempt to connect, timemout after 1 second (move on)
		result = s.connect_ex((target,port)) #Returns an error indicator (0 or 1)
		if result == 0:
			print("Port {} is open".format(port))
		s.close() #Close connection

#Ctrl-C		
except KeyboardInterrupt: 
	print("\nExiting program..")
	sys.exit()
	
#No hostname resolution, exit program
except socket.gaierror:
	print("Hostname could not be resolved.")
	sys.exit()

#Can't locate IP address, exit program
except socket.error:
	print("Couldn't connect to server.")
