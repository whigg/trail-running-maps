#!/bin/bash
datadir="/home/ctroupin/Projects/Leaflet/GranCanariaActivity/data/"
for ff in $(ls ${datadir})
  do
  year=$(grep '<time>' -m 2 ${datadir}${ff} | tail -1 | cut -d '>' -f2 | cut -d '-' -f1)
  mkdir -pv ${datadir}${year}
  mv ${datadir}${ff} ${datadir}${year}
done

