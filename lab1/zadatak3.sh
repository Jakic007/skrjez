#!/bin/bash

for file in $(ls *-02-*.txt);
do
    d=`echo $file | cut -d "-" -f 1`
    m=`echo $file | cut -d "-" -f 2`
    y=`echo $file | cut -d "-" -f 3 | cut -d "." -f 1`
    
    echo "datum: $d-$m-$y"
    
    echo "------------------------------------------------------"
    
    cat $file | cut -f 2 -d \"| sort | uniq -c | sort -n -r | sed -r 's/([0-9]+)(.*)/\1 : \2/'
    
done