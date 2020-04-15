#!/bin/bash

if [ "$#" -lt 2 ]
then
    echo "Potrebna su najmanje dva parametra. Primjer:"
    echo "./zadatak6.sh datoteka1 .backup/"
    exit
fi

if [ ! -d ${!#} ]
then
    mkdir -p ${!#};
    echo "stvoreno kazalo"
fi
brojac=0
for file in $@;
do
    if [[ $file == ${!#} ]]
    then
        echo kraj
        echo "prebaceno je $brojac datoteka"
        exit
    fi
    if [[ -r $file ]]
    then
        mv $file ${!#}/$file
        brojac=$((brojac + 1))
    else
        echo "datoteka $file nije citljiva"
    fi
    
done
