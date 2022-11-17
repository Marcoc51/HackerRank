#! /bin/bash

readarray -t arr
arr=("${arr[@]}" "${arr[@]}" "${arr[@]}")
echo "${arr[@]}"
