#!/usr/bin/bash


# installing python by checking the exit status


if [ $? -eq 0 ]
then
	yum install python3
else
	echo "you need to have root privilages to execute the command"
fi
