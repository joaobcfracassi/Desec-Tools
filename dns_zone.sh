#!/bin/bash

HOSTS=$(host -t ns businesscorp.com.br)

for SERVERS in $HOSTS;
do
	host -l -a businesscorp.com.br $SERVERS;
done
