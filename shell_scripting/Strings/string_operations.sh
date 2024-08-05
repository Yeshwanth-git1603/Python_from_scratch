#!/usr/bin/bash

# string operations

string="Shellscripting"
echo "${string}"
echo "${string^^}"
echo "${string,,}"
echo "${string:0:5}"

for str in "${string}"
do
	echo "$str"
done


