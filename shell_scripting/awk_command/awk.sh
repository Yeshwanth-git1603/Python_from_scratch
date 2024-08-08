#!/usr/bin/bash


httpd -v | awk -F '[ /]' '/version/ {print $4}'
