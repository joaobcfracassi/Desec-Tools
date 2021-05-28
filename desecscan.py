#!/usr/bin/python

import sys
from scapy.all import *

#conf.verb = 0

portas = [21,22,23,25,80,443,110]

pIP = IP(dst=sys.argv[1])
pTCP = TCP(dport=portas,flags="S")
pacote = pIP/pTCP
resp, noresp = sr(pacote)

for resposta in resp:
	porta = resposta[1][TCP].sport
	flag = resposta[1][TCP].flags
	#print ("%d %s" %(porta,flag))
	
	if (flag == "SA"):
		print ("Porta %d ABERTA" %(porta))