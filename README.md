# trail-running-maps
Tracks and heatmaps using the GPS tracks. 

The code use the fabulous [folium](https://pypi.python.org/pypi/folium) package (version 0.2.0) that allows us to interact with the [leaflet](http://leafletjs.com/) library.

![Running in Gran Canaria](./images/grancanaria_heatmap.png?raw=true "Gran Canaria" {width=300px})

The GPX tracks are either
* downloaded from my [http://www.wikiloc.com/](wikiloc) account,
* converted from the Garmin .fit files using the [gpsbabel](http://www.gpsbabel.org/) tool.

The coordinates and the track name are extracted from the GPX files using regular expressions.
