#!/usr/bin/bash

user_id=$(id -u)

if [ $user_id -eq 0 ]
then
	sudo su -
else
	echo "$(date)"
fi

for x in $(ls -ltr)
do
	echo "$x"
done


