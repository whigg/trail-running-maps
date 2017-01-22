#!/bin/bash

if [ "$#" == "0" ]
  then 
  echo 'Usage: ./makeList.bash inputdir outputfile movename'
  stop 
  else if [ "$#" == "1" ]
  then
  inputdir=$1
  outputfile='./'
  movename='moves'
  else if [ "$#" == "2" ] 
  then
  inputdir=$1
  outputfile=$2
  movename='moves'
  else if [ "$#" == "3" ]
  then
  inputdir=$1
  outputfile=$2
  movename=$3
  fi
  fi
  fi
fi

echo "var" ${movename} "= [" > ${outputfile}
find ${inputdir} -maxdepth 1 -type f -name '*gpx' -printf '"%p",\n' >> ${outputfile}
echo "]" >> ${outputfile}

