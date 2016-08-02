# trail-running-maps
Tracks and heatmaps using the GPS tracks. 

The code use the fabulous [folium](https://pypi.python.org/pypi/folium) packages that allows us to interact with the [leaflet](http://leafletjs.com/) library.

The GPX tracks are either
* downloaded from [http://www.wikiloc.com/](wikiloc),
* converted from the Garmin .fit files using the [gpsbabel](http://www.gpsbabel.org/) tool.

The coordinates and the track name are extracted from the GPX files using regular expressions.
