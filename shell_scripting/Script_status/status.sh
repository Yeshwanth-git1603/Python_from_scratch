#!/usr/bin/bash

set -e

Date=$(date)

echo "$Date"

if [ $? -eq 0 ]
then
	echo " today date is:$Date "
else
	echo "incorrect command"
fi

User_id=$(id -u)

echo "$User_id"

if [ $User_id -ne 0 ]
then
	sudo su -
else
	echo" command not found "
fi

user_name=$(uname)

if [ $user_name -eq 0 ]
then
	ls -ltr
else
	echo "command is not found"
fi

