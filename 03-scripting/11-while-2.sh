#/bin/bash

counter=1

while true
do 
	echo "counter is $counter"
	counter=$(( $counter * 2 ))
	

	if [ $counter -eq 100 ]
	then 
	break
	fi	
done

echo "while loop ended"

