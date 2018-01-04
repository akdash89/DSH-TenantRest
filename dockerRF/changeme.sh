#!/bin/bash

IP=`ifconfig | grep inet | grep -v inet6 | head -1 | awk '{print $2}' | cut -d':' -f2`
sed -i -e "s/IPADDRESS/$IP/g" "makefile"