#!/bin/bash

if [ "$#" -eq "1" ]; then
  N=$1
else
  N=500
fi

GPSBABEL='/usr/bin/gpsbabel'

for gpx in $(ls */*.gpx)
do
  ${GPSBABEL} -r -i gpx -f ${gpx} -x simplify,count=${N} -o gpx -F ${gpx}
done
