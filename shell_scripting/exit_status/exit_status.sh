#!/usr/bin/bash

user_id=$(id -u)

if [ $user_id -eq 0 ]
then
	yum update -y
else
	echo "you need to switch as root user for executing the cmd"
fi

process=$(nproc)

echo "the vm is using $process this many process for a VM"


