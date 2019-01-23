#!/usr/bin/python
import socket
import sys

# Handle argument
if len(sys.argv) < 3:
	print >>sys.stderr, "Usage: master-parrot [PORT] [PARTY_TIME]"
	exit(-1)
port = int(sys.argv[1])
party_time = int(sys.argv[2])

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address given on the command line
server_address = ("0.0.0.0", port)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)
sock.listen(1)

while True:
	connection, client_address = sock.accept()
	try:
		print >>sys.stderr, 'parrot connected:', client_address
		while True:
			data = connection.recv(1024)
			if data.startswith("PARROT HELLO"):
				connection.sendall("LET'S PARTY AT {}!".format(party_time))
				print >>sys.stderr, 'PARROT PARTYING!'
				break
			else:
				break
	finally:
		connection.close()

