#!/bin/bash

#sort based on first column considering it as a number
sort -n -k1,1 $1 > "sorted_$1"
echo "data sorted"
