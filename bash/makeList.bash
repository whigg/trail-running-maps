#!/bin/bash
inputdir=$1
outputfile=$2

echo "var moves = [" > ${outputfile}
find ${inputdir} -maxdepth 1 -type f -name '*gpx' -printf '"%p",\n' >> ${outputfile}
echo "]" >> ${outputfile}

