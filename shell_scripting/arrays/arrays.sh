#!/usr/bin/bash

array1=(1 2 3 4 5)
echo "${array1[@]}"

for x in {1..5}
do
	echo "${array1[@]}"
done

for y in "${array[@]}"
do
	echo "$y"
done

array2["name"]="yeshwanth"
array2["age"]="23"
array2["height"]="5.9"

echo "${array2[@]}"

declare -A array3

array3["name"]="yeshwanth"
array3["age"]="23"

echo "${array3[@]}"
