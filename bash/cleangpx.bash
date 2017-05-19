#!/bin/bash

# Read a GPX file and create a new one containing only the successive positions.
#
# The GPX downloaded from Garmin or Movescount are often much bigger than necessary
# because of information stored in <extension> tags. 
# The script use 'sed' to remove what lies within these tags.


TAG='extensions'
for files in "$@"
do
    outdir=$(dirname ${files})
    outputfile=${outdir}'/'$(basename -s '.gpx' ${files})'_noext.gpx'
    echo "cat ${files} | sed -e '/<${TAG}>/, /<\/${TAG}>/ d ' > ${outputfile}"
done
#cat config.xml-ori | sed -e '/<app-tag>/, /<\/app-tag>/ d ' > config.xml


