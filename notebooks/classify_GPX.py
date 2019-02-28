
import gpxpy
import gpxpy.gpx
import numpy as np
import os
import glob
import logging
from geopy import distance


def get_mean_coord(filename):
    with open(filename, "r") as gf:
        gpx = gpxpy.parse(gf)
        lon = []
        lat = []
        for track in gpx.tracks:
            for segment in track.segments:
                for point in segment.points:
                    lon.append(point.longitude)
                    lat.append(point.latitude)
        if len(lon) > 0:
            lon = np.array(lon)
            lat = np.array(lat)
            lonmean = lon.mean()
            latmean = lat.mean()
        else:
            lonmean = np.nan
            latmean = np.nan

    return lonmean, latmean



def make_place_dict():
    # Dictionary storing the places: keys = names
    # values = tuple with lon, lat or mean location and max. distance from mean location
    locDict = {"verviers": (50.583333, 5.85, 15.),
               "sarttilman": (50.581546, 5.567365, 7.),
               "piran": (45.523821, 13.567222, 10.),
               "grancanaria": (28.049768, -15.575252, 30.),
               "barcelona": (41.383333, 2.183333, 10.),
               "ostende": (51.233333, 2.916667, 10.),
               "lapalma": (28.666667, -17.866667, 20.),
               "tenerife": (28.268611, -16.605556, 50.),
               "elhierro": (27.75, -18, 15.),
               "delft": (52.011736, 4.359208, 5.),
               "hamburg": (53.565278, 10.001389, 7.),
               "calvi": (42.5686, 8.7569, 7.),
               "athens": (37.976354, 23.726661, 10.),
               "mallorca": (39.624293, 3.025380, 30.),
               "boulder": (40.014196, -105.262618, 10.),
               "porto": (41.162142, -8.621953, 10.)
               }
    return locDict

def main():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logging.info("starting")

    year = "2019"
    gpxdir = "/data/GPX/2class/{}/".format(year)
    filelist = sorted(glob.glob(os.path.join(gpxdir, "{}*.gpx".format(year))))
    nfiles = len(filelist)
    if nfiles == 0:
        logger.warning("No files in this directory")
    else:
        logging.info("Working on {} GPX files".format(len(filelist)))

        locDict = make_place_dict()

        for gpxfile in filelist:
            fname = os.path.basename(gpxfile)
            logger.debug("Working on file {}".format(fname))
            # Check file size
            if os.stat(gpxfile).st_size > 0:
                lonmean, latmean = get_mean_coord(gpxfile)
                if not(np.isnan(lonmean)):
                    # loop over the places
                    for city, coords in locDict.items():
                        if not(np.isnan(lonmean)):
                            dist = distance.distance((latmean, lonmean), (coords[0], coords[1])).km
                            if dist < coords[2]:
                                logger.info("Closest place: {}".format(city))
                                newfilename = "_".join((city, fname))
                                logger.debug("New file name {}".format(newfilename))
                                os.rename(gpxfile, os.path.join(gpxdir, newfilename))
                        else:
                            logger.info("Not a running activity")
                            os.remove(gpxfile)
                else:
                    os.remove(gpxfile)
            else:
                logger.debug("File is empty")
                os.remove(gpxfile)


if __name__ == "__main__":

    main()
