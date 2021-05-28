#!/usr/bin/python

import socket,sys

ip = sys.argv[1]

portas = [22,23,25,80,443,8080,8443]

for ip in range(1,254):
	iprange = "192.168.0.%s" %(ip)
	meusocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	if meusocket.connect_ex((iprange,portas)) == 0:
		print "Porta",portas,"[ABERTA]"
		meusocket.close()
