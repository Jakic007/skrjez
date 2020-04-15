#!/bin/bash


proba="Ovo je proba"

echo $proba

lista_datoteka="Lista datoteka u tekucem kazalu je: $(ls)"
echo $lista_datoteka

proba3="$proba. $proba. $proba."

a=4
b=3
c=7
d=$((($a+4)*$b%$c))

broj_rijeci=`(cat *.txt | wc -w)`
echo $broj_rijeci

ls ~

cut -d ':' -f 1,6,7 /etc/passwd

ps -f | cut -d ' ' -f 1,3,14 | tail -n +2