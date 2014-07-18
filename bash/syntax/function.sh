#!/bin/bash

# Let your code speak

is_dir()
{
    local dir=$1
    [[ -d $dir ]]
}

main()
{
    local dir=/tmp
    if is_dir $dir; then
        echo "this is dir, i can do something..."
    fi
}

main
