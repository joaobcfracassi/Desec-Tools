#!/bin/bash

for SUBDOM in $(cat lista.txt);
do
	host -t cname $SUBDOM.$1 | grep "alias for";
done
