#!/usr/bin/env bash
set -e

# there is a difference run type command in bash and script
# but why ?
type -t tmux

res=$(type -t tmux)
echo $res

res2=`type -t cd`
echo $res2

if [[ $(type -t tmux) == "alias" ]]; then
    echo "tmux has alias"
fi
