#!/usr/bin/bash


set -e


arithmetic()
{
	m=$1
	n=$2
	read -p "enter A value:" m
	read -p "enter B value: " n
	sum=$((m+n))
	echo " the sum of $m and $n is $sum "

}


arithmetic $a $b


subtraction()
{
	m=$1
	n=$2
	read -p "enter A value:" m
	read -p "enter B value: " n
	sub=$((m-n))
	echo " the sub of $m and $n is $sub "

}

subtraction $a $b
