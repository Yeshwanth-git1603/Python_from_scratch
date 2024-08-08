#!/usr/bin/bash


##using awk command we are printing only the version of the apache server

httpd -v | awk -F '[ /]' '/version/ {print $4}'


