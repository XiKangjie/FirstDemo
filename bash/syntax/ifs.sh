#!/bin/bash

# IFS is the Internal Filed Separator.
# The default value is SPACE TAB NEWLINE.

OLD_IFS="$IFS"
IFS=:
echo "Please input three data separated by colons ..."
read x y z
IFS="$OLD_IFS"
echo "x is $x, y is $y, z is $z"
