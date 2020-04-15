#!/bin/bash

grep -iE "banana|jabuka|jagoda|dinja|lubenica" namirnice.txt

grep -ivE "banana|jabuka|jagoda|dinja|lubenica" namirnice.txt > ne-voce.txt

grep -d recurse -E '([[:upper:]]{3}[[:digit:]]{6})' ~/projekti

find ./ -mtime +7 -mtime -14

for i in `seq 1 15`; do echo $i; done