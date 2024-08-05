#!/usr/bin/bash

#node health check

#author Yeshwanth k
#date 04.08.2024


set -x
set -e
ps  -ef | grep "amazon" 

df -h
 
free -g

nproc 

finger
