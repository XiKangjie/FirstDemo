#!/bin/bash

# useful trick of while loop

FILE_NAME=$1
while read line
do
    echo "$line"
done < "$FILE_NAME"

