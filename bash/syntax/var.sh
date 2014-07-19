#!/bin/sh

echo "What is your name?"
read USER_NAME
echo "What is your gender?"
read USER_GENDER
echo "How old are you?"
read USER_AGE
echo "Hello $USER_NAME"
echo "You're ID is ${USER_NAME}${USER_GENDER}${USER_AGE}"

