#!/bin/bash

A="I'm a"
for var in A "A" 'A' "$A"; do
    echo "var is "$var""
done
