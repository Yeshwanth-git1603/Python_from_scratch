#!/usr/bin/bash

for x in {1..100}
do
	if [ `expr $x  % 3 = 0` || `expr $x % 5 = 0` ] && [ `expr $x!=15` ]
	then
		echo "$x"
	else
		echo "exit"
	fi
done
