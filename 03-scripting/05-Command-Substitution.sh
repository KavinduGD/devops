#!/bin/bash

echo "Welcome $USER on $HOSTNAME"
echo "#################################################################"

FREERAM=$(free -m  | grep Mem | awk '{print $4}')
LOAD=`uptime | awk '{print $9}'`


echo "Free ram : $FREERAM"
echo "LOAD is $LOAD"
