#!/bin/bash

if [ "$#" -ne 1 ]
then
    echo "Potreban je parametar. Primjer:"
    echo "./zadatak4.sh studenti.txt"
    exit
fi

cat $1 | sed -E 's/;/ /g' | awk '{arr[$5]+=$4} END {for (i in arr) {print i":" ,arr[i]}}' | sort -nk 2
