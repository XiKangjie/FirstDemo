#!/usr/bin/env bash

A="I'm a"
for var in A "A" 'A' "$A"; do
    echo "var is "$var""
done
#var is A
#var is A
#var is A
#var is I'm a


for i in {0..10..2}; do
    echo $i
done
#0
#2
#4
#6
#8
#10


for ((i=0; i<5; i++)); do
    echo $i
done
#0
#1
#2
#3
#4


#list files
for f in *; do
    echo $f
done
