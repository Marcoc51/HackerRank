#! /bin/bash

while read line
do
    arr=("${arr[@]}" $line)
done

echo "${#arr[@]}"
