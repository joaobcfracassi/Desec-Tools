#!/bin/bash

for ip in $(seq 1 154);do
	arping -c 1 $1.$ip;
done | grep "60 bytes" 
