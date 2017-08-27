#!/bin/bash

GPSBABEL='/usr/bin/gpsbabel'

re='^[0-9]+$'

# If last element is an integer,
# then it's the number of points for the subsampling
#
#if ! [[ "${@: -1}" =~ "$re" ]] ; then
#  echo "that's an integer"
#  N=${@: -1}
#else
#  N=500  
#fi

N=500
for gpx in $@ ; do
  if [ -f ${gpx} ]; then 
    gpxout=${gpx%.*}"_500pts.gpx"
    "${GPSBABEL}" -r -i gpx -f "${gpx}" -x simplify,count="${N}" -o gpx -F "${gpxout}"
  else
    echo "${gpx}" "doesn't exist"
  fi
done
