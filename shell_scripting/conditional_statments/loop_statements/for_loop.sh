#!/usr/bin/bash


for x in {1..10}
do
	echo "$x"
done

array1=(1 2 3 4 5)
array1+=(6 7 8 9 10)
echo "${array1[@]}"

echo "${array1[*]}"

echo "${!array1[*]}"
