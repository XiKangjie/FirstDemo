#!/usr/bin/env bash
set -e

myvar=sometext

# single quotes preserves the literal value of each character within the quotes.
echo 'single quotes gives you $myvar'

# double quotes
echo "double quotes gives you $myvar"

#single quotes gives you $myvar
#double quotes gives you sometext
