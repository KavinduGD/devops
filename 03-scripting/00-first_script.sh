#!/bin/bash

### This script displays system info ####


echo "Welcome to the first bash script"
echo 
echo "###################################"
# Displays system info
echo "The up time is"
uptime
echo
echo "###################################"


# displays memoty utilization
echo "Memory utilization"
free -m
echo
echo "###################################"

# Display disk utlization
echo "Dick utilization"
df -h
echo
echo "###################################"
