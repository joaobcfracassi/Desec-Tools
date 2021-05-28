#!/bin/bash

for SUBDOM in $(cat lista.txt);
do
	host $SUBDOM.$1 | grep -v "NXDOMAIN";
done
