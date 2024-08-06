#!/usr/bin/bash

memory=$(df)

if [ $? -eq 0 ]
then
	echo "$memory"
else
	echo "you need to change the exit status of the command first"
fi


