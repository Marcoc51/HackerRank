#! /bin/bash

awk '{
if (($2 + $3 + $4)/3 >=80)
    print $1, $2, $3, $4, ": A";
else if (($2 + $3 + $4)/3 >=60)
    print $1, $2, $3, $4, ": B";
else if (($2 + $3 + $4)/3 >=50)
    print $1, $2, $3, $4, ": C";
else 
    print $1, $2, $3, $4, ": FAIL"
}'
