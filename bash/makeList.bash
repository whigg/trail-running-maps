#!/bin/bash

# Create list in json from files inside a given directory
# ctroupin 2017
# 

case $# in 
0)
    echo "Usage: ${0} inputdir outputfile movename"
    exit 1
    ;;
1)
    inputdir=$1
    outputfile='moves.js'
    movename='moves'
    ;;
2)
    inputdir=$1
    outputfile=$2
    movename='moves'
    ;;
3)
    inputdir=$1
    outputfile=$2
    movename=$3
    ;;
*)
    echo "Too many input arguments"
    exit 1
    ;;
esac

echo "var" ${movename} "= [" > ${outputfile}
#find ${inputdir} -maxdepth 1 -type f -name '*gpx' -printf '"%p",\n' >> ${outputfile}

for f in $(ls -tr ${inputdir}/*.gpx); do
  printf "'$(basename ${f})',\n" >> ${outputfile}
done

echo "]" >> ${outputfile}

