#!/bin/bash

# Read a GPX file and create a new one containing only the successive positions.
#
# The GPX downloaded from Garmin or Movescount are often much bigger than necessary
# because of information stored in <extension> tags. 
# The script use 'sed' to remove what lies within these tags.
TAG='extensions'
cat config.xml-ori | sed -e '/<app-tag>/, /<\/app-tag>/ d ' > config.xml


