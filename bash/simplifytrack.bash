#!/bin/bash

GPSBABEL='/usr/bin/gpsbabel'

re='^[0-9]+$'

# If last element is an integer,
# then it's the number of points for the subsampling

if ! [[ "${@: -1}" =~ "$re" ]] ; then
  echo "that's an integer"
  N=${@: -1}
else
  N=500  
fi


for gpx in $@ ; do
  if [ -f ${gpx} ]; then 
    echo "ok ok ok" 
    echo ${GPSBABEL} -r -i gpx -f ${gpx} -x simplify,count=${N} -o gpx -F ${gpx}
  fi
done
