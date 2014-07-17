#!/bin/bash

help()
{
cat << HELP
    This is a generic command line parse demo.
    USAGE EXAMPLE: ./option.sh -n "consen" -m -- 25
HELP
    exit 0
}

while [ -n "$1" ]; do
    case "$1" in
        -h) help; shift 1;;             # function help is called
        -n) name="$2"; shift 2;;        # -n takes an argument -> shift by 2
        -m) gender="male"; shift 1;;
        -f) gender="female"; shift 1;;
        --) shift; break;;              # end of options
        -*) echo "error: no such option $1. -h for help"; exit 1;;
        *) break;;
    esac
done

echo "your name is $name and gender is $gender"
echo "first arg is $1"
echo "2nd arg is $2"

