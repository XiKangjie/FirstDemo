#!/bin/bash

# '[' is actually a program, just like ls and other programs, so it must
# besurrounded by spaces:
# if SPACE [ SPACE "$foo" SPACE = SPACE "bar" SPACE ]

# be aware of the syntax -- the "if [ ... ]" and "then" commands must be
# on different lines. Alternatively, the semicolon ";" can separate them:
# if [ ... ]; then

echo -en "Please guess the magic number: "
read X
echo "$X" | grep "[^0-9]" > /dev/null 2>&1
if [ "$?" -eq "0" ]; then
    # If the grep found something other than 0-9
    # then it's not an integer.
    echo "Sorry, wanted a number"
else
    # The grep found only 0-9, so it's an integer.
    # We can safely do a test on it.
    if [ "$X" -eq "7" ]; then
        echo "You entered the magic number!"
    fi
fi
