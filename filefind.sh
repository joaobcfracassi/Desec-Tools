#!/bin/bash

lynx -dump "http://google.com/search?num=100&q=site:"$1"+ext:"$2"" | cut -d "=" -f 2 | grep ".$2" | egrep -v "site|google" | sed s"/...$//"