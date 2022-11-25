#! /bin/bash

read len
readarray -t arr
sum=0
for i in "${arr[@]}"
do
    sum=`expr $sum + $i`
done
printf "%.3f" $(echo "$sum / $len" | bc -l)
