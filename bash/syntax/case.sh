#!/bin/bash

HELLO="hello"
echo "Please talk to me..."
while :
do
    read INPUT_STRING
    case $INPUT_STRING in
        $HELLO)   # followed by a right bracket
            echo "Hello yourself!"
            ;;     # section of code is executed, up to the double semicolon
        bye)
            echo "See you again!"
            break
            ;;
        "I love you")
            echo "I love you too!"
            ;;
        *)
            echo "Sorry, I don't understand!"
            ;;
    esac
done

echo
echo "Thast's all folks!"
        
