#!/bin/bash

GPSBABEL='/usr/bin/gpsbabel'

N=500

for gpx in $@ ; do
  if [ -f ${gpx} ]; then 
    gpxout=${gpx%.*}"_"${N}"pts.gpx"
    "${GPSBABEL}" -r -i gpx -f "${gpx}" -x simplify,count="${N}" -o gpx -F "${gpxout}"
  else
    echo "${gpx}" "doesn't exist"
  fi
done
