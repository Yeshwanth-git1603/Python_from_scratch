#!/usr/bin/bash

# finding the process ids by using awk command
# using field separator and using root field to find the id's

ps -ef | awk -F " " '/root/ {print $2}'
echo 
#finding the available memory using the awk command
#using field separator to find the field 'avail' and using the string tmpfs


echo "disk fragmentation"

df -h | awk -F " " '/tmpfs/ {print $4}'


# using the NR 'number of records' to find the exact field
# here we are using free command for reference


echo "using free command"

free -h | awk -F " " 'NR==1{print $3}'

free -h | awk -F " " 'NR==2{print $3}'

free -h | awk -F " " 'NR==3{print $3}'

# usinf the NF " no of fields we can know how many fields are there in the command


echo "using free command"

free -h | awk -F " " '{print NF}'





