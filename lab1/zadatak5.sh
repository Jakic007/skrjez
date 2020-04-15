#!/bin/bash

if [ "$#" -ne 2 ]
then
    echo "Potrebna su dva parametra. Primjer:"
    echo "./zadatak5.sh /kazalo uzorak"
    exit
fi
echo "argumenti su $1 i $2"
lines=0
for dir in $(find $1 -type d);
do
    
    for file in $(find $dir -maxdepth 1 -type f)
    do
        if [[ $file == $2 ]]
        then
            lines=$((lines + `cat $file | wc -l`))
        fi
    done
    
done
echo $lines