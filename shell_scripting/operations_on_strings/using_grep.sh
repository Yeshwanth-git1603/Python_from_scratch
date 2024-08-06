#!/usr/bin/bash


# performing string operations and finding the characters in the string


x=mississippi
echo "for x string"
grep -o "s"<<<$x | wc -l

y=hellotherehowareyouareyoufine
echo "for y string"
grep -o "y"<<<y | wc -l


z=hellogoodmorninghowareyoudoingtoday
echo "for z string"
grep -o "m"<<<z | wc -l


