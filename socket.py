#!/usr/bin/python

import socket
import sys

ip = raw_input("Digite o IP:")
porta = int(raw_input("Digite a porta:"))

meusocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

resp = meusocket.connect_ex((ip,porta))

if(resp == 0):
	print "Porta aberta"
else:
	print "Porta fechada"