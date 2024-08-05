#!/usr/bin/bash
set -x
set -e
auth()
{
	m=$1
	n=$2

	read -p " enter the username " m
	read -p "enter the password" n
	echo "authentication successfull"
}



auth $p $q

