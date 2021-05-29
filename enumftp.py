#!/usr/bin/python

import socket

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.connect(("172.16.1.108",21))
print "Conectando ao servidor..."
banner = tcp.recv(1024)
print banner

print "Enviando o usuario..."
tcp.send("USER ftp\r\n")
user = tcp.recv(1024)
print user

print "Enviando a senha..."
tcp.send("PASS ftp\r\n")
pw = tcp.recv(1024)
print pw

print "Enviando um comando HELP..."
tcp.send("HELP\r\n")
cmd = tcp.recv(2048)
print cmd

