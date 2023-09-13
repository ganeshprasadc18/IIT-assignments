#!/bin/bash

#get first argument as filename to be saved and the second as the number of records to be produced
nameofnewfile="$1"
recordcount="$2"

#getting the start time of generating records
start_time=$(date +%s)

#generate the dataset in <integer> <integer> <ASCII_string>
while [ "$(($(date +%s) - start_time))" -lt 10 ]; do
	for ((i=0; i< recordcount; i++)); do
		echo "$((RANDOM * RANDOM)) $((RANDOM * RANDOM)) $(head -c 100 /dev/urandom | tr -dc '[:print:]')"
	done
done > "$nameofnewfile"


