#!/usr/bin/python

from scapy.all import *

conf.verb = 0

print ("Hosts Ativos:")
for ip in range(1,255):
	iprange = "192.168.0.%s" %(ip)
	#print (iprange)
	pIP = IP(dst=iprange)
	pacote = pIP/ICMP()
	resp,noresp = sr(pacote,timeout=1)
	print (resp.show())
	#print (resp[0][1].show() )

	for resposta in resp:
		print (resposta[1][IP].src)
