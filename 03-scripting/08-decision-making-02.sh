#/bin/bash

NETWORKS=$(ip addr | grep mtu | grep -cv LOOPBACK)

if [ $NETWORKS -eq 1 ]
then 
	echo "You have 1 adapter"
elif [ $NETWORKS -gt 1 ]
then
	echo "You have more than 1 networks"
else
	echo "You have less than 1 network"
fi
