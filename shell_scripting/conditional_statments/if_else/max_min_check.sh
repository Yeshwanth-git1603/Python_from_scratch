#!/usr/bin/bash

read -p "enter a value" a
read -p "enter b value" b

if [ $a -gt $b ]
then
	echo "$a is greater"
else
	echo "$b is greater"
fi

read -p "enter x value" x
read -p "enter y value" y
read -p "enter z value" z

if [ $x -gt $y -a $x -gt $z ]
then
	echo "$x is greater"
elif [ $y -gt $z ]
then
	echo "$y is greater"
else
	echo "$z is greater"
fi

