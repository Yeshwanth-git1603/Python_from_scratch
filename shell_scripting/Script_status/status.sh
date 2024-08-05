#!/usr/bin/bash

set -e
set -x

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


