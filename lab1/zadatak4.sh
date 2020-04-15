#!/bin/bash

if [ "$#" -ne 2 ]
then
    echo "Potrebna su dva parametra. Primjer:"
    echo "./zadatak4.sh /izvorni_direktorij/ /odredisni_direktorij/"
    exit
fi

if [ ! -d $2 ]
then
    mkdir $2
fi

for file in $(ls ./"$1");
do
    dirName=$(stat -c %y "./$1/$file" | cut -d "-" -f 1,2);
    echo $dirName;
    if [ ! -d $2/$dirName ]
    then
        mkdir -p ./"$2"/"$dirName";
    fi
    
    mv "./$1/$file" ./"$2"/"$dirName"/"$file";
done