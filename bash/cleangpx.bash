#!/bin/bash

# Read a GPX file and create a new one containing only the successive positions.
#
# The GPX downloaded from Garmin or Movescount are often much bigger than necessary
# because of information stored in <extension> tags. 
# The script uses 'sed' to remove what lies within these tags.

# need to add something to check if at least one file exists in $@

TAG='extensions'

if [ "$#" == "0" ]
then
    echo "Usage: ${0} files"
    exit 1
fi

for files in "$@"
do  
    outdir=$(dirname ${files})
    outputfile=${outdir}'/'$(basename -s '.gpx' ${files})'_no'${TAG}'.gpx'
    echo ${files} '-->' ${outputfile}
    cat ${files} | sed -e "/<${TAG}>/, /<\/${TAG}>/ d " > ${outputfile}
done


