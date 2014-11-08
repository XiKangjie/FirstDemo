#!/usr/bin/env bash

set -e

# hash return status is true unless the name is not found in $PATH
function command_exists {
    hash "$1" 2>/dev/null
}

if command_exists git; then
    echo "git has been installed."
else
    echo "you should install git first."
fi
