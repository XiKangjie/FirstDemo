#!/bin/bash

# useful trick of while loop

FILE_NAME=$1
while read line
do
    if [[ -n $line && $line != "#"* ]]; then
        echo "$line"
    fi
done < "$FILE_NAME"

