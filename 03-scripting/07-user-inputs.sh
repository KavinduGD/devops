#/bin/bash

echo "####################### User Inputs"
echo

echo "Enter your subject : "
read SUBJECT
echo "Recieved the subject, you have entered $SUBJECT"
echo 

echo "Lets enter your username and password"
read -p "Username : " USER_NAME
read -sp  "Password : " PASSWORD
echo

echo "Welcome back $USER_NAME"

