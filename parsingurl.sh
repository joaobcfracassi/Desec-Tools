#!/bin/bash
if [ "$1" == "" ]; 
then
	echo "DESEC SECURITY - PARSING URL"
	echo "Modo de uso: $0 SITE"
	echo "Ex: $0 www.businesscorp.com.br"
else
	site=$1
	wget $site
	grep href index.html | cut -d "/" -f 3 | grep "\." | cut -d '"' -f 1 | grep -v "<l" > lista.txt
	for host in $(cat lista.txt );
	do 
		host $host | grep -v "not found";
	done
fi