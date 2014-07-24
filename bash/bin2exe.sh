#! /bin/bash
# rename executable file to file.exe

filelist=$(ls)                      # no spaces on both sides of '='
for filename in $filelist
do
    if [ -x $filename ]; then
        mv $filename ${filename}.exe
    fi
done
