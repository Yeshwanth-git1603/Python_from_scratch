#!/usr/bin/bash


read -p "enter a value " a
read -p "enter b value"  b
read -p "enter the option(1.add,2.sub,3.mul,4.div,5.remainder) " opt

case $opt in
	1)
		echo "you selected add"
		echo "the sum of $a and $b is $((a+b))"
		;;
	2)
		echo "you selected sub"
		echo "the sub of $a and $b is $((a-b))"
		;;
	3)
		echo "you selelcted mul"
		echo "the prod of $a and $b is $((a*b))"
		;;
	4)
		echo "you selelcted div"
		echo "the div of $a and $b is $(bc<<<"scale=2;$a/$b")"
		;;

	5)
		echo "you selected remainder"
		echo "the remainder of $a and $b is $((a%b))"
		;;
	*)
		echo "enter the valid option"
		;;
esac
