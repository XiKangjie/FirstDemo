#!/usr/bin/env bash

set -e

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

print_cpu_percentage() {
    if [ -e "/proc/stat" ]; then
        # just the last cpu!
        grep 'cpu ' /proc/stat | awk '{usage=($2+$4)*100/($2+$4+$5)} END {printf("%5.1f%\n", usage)}'
    fi
}

main() {
    print_cpu_percentage
}

main
