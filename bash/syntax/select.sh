#!/bin/bash

#select var in ... ; do
#    　break;
#done
#.... now $var can be used ...

#
# will not check error!
#
echo "What is your favourite OS?"
select var in "Linux" "Windows" "IOS"; do
    break;
done
echo "You have selected $var"
