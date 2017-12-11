#!/bin/env/bash

set -e

count=$1

for ((i=0; i<$count; i++)); do
    python push.py
done
