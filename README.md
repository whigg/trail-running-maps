# Trail running maps

A collection of tools in bash, python and javascript to process and display GPS tracks from different devices.

## Data files

The tracks in GPX format are either
* directly downloaded from [http://www.wikiloc.com/](wikiloc) or from [http://movescount.com/](movescount) or
* converted from the Garmin `.fit` files using the [gpsbabel](http://www.gpsbabel.org/) tool.

## Python

The scripts use the fabulous [folium](https://pypi.python.org/pypi/folium) package that allows the interaction with the [leaflet](http://leafletjs.com/) library.

<img src="./images/grancanaria_heatmap.png " width="400">


The coordinates and the track name are extracted from the GPX files using regular expressions.
