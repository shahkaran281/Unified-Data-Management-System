#!/bin/sh
echo ${2}
echo ${1}
# sed '${1}d' ${2} 
sed "${1}d" ${2}  > data/tmpfile 
mv data/tmpfile ${2}

