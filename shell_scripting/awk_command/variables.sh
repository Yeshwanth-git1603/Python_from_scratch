#!/usr/bin/bash

#printing variables using awk command


read -p "enter a value" a
read -p "enter b value" b

echo "$a $b" | awk '{x=$1; y=$2; print "sum=" x+y}'


read -p "enter a value" a
read -p "enter b value" b

echo "$a $b" | awk '{x=$1;y=$2; print "sub=" x-y}'


read -p "enter a value" a
read -p "enter b value" b

echo "$a $b" | awk '{x=$1;y=$2; print "div=" x/y}'


read -p "enter a value" a
read -p "enter b value" b

echo "$a $b" | awk '{x=$1;y=$2; print "mul=" x*y}'
