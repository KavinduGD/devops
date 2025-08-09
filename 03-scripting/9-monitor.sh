#/bin/bash

echo "####################################################################################"
date

if [ -f /var/run/httpd/httpd.pid ]
then
	echo "httpd is running"
else 
	echo "httpd is not running"
	echo "http service starting"
	systemctl start httpd 

	if [ $? -eq 0 ]
	then
		echo "httpd started successfully"
	else
		echo "http start failed"
	fi
fi

echo "#####################################################################################"
