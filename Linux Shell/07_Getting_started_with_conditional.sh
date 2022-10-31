#!/bin/bash
read char
if [[ $char == "Y" || $char == "y" ]]
then
echo "YES"
else
echo "NO"
fi
