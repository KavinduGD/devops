#!/bin/bash

echo "############ Decision making ###############"
echo

read -p "Enter a number : " NUMBER

if [ $NUMBER -gt 100 ]
then
	echo "Number is greater than 100"
else
	echo "Number is less than 100"
fi

echo "Operation completed"
