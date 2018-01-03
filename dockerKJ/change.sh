#!/bin/bash

dMDisk = "/home/rakeshlaptop/Documents/projects/DSH/mountedDisk"
IP=`ifconfig | grep inet | grep -v inet6 | head -1 | awk '{print $2}'`
IPREAL = "$(cut -d':' -f2 <<<"$IP")"
echo $IP
sed -i -e "s/IPADDRESS/$IP/g" "py/TenantRestConfig.py"