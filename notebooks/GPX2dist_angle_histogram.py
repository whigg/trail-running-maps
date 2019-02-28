# Plot a polar pseudo-color plot using a list of GPX

import gpxpy
import gpxpy.gpx
import numpy as np
import os
import glob
import logging
from geopy import distance
from geo import sphere
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import matplotlib.patheffects as PathEffects
fa_dir = r"/home/ctroupin/Downloads/fontawesome-free-5.0.13/use-on-desktop/"
fp1 = FontProperties(fname=os.path.join(fa_dir, "Font Awesome 5 Free-Solid-900.otf"))
import cmocean
import warnings
import matplotlib.cbook
warnings.filterwarnings("ignore",category=matplotlib.cbook.mplDeprecation)

def get_coords(filename):
    """
    Get the coordinates and the elevation from a GPX file
    """
    with open(filename, "r") as gf:
        gpx = gpxpy.parse(gf)
        lon = []
        lat = []
        ele = []
        for track in gpx.tracks:
            for segment in track.segments:
                for point in segment.points:
                    lon.append(point.longitude)
                    lat.append(point.latitude)
                    ele.append(point.elevation)
        lon = np.array(lon)
        lat = np.array(lat)
        ele = np.array(ele)

    return lon, lat, ele

def get_distance_bearing(filelist, lon0, lat0, logger):
    """
    Compute the distances and bearing from a list
    of GPX files.
    Return 2 arrays
    """
    distancevec = []
    bearingvec = []
    elevations = np.array([])

    for gpxfile in filelist:
        logger.debug("Working on {}".format(gpxfile))
        fname = os.path.basename(gpxfile)

        # Check file size
        if os.stat(gpxfile).st_size > 0:
            lon, lat, ele = get_coords(gpxfile)
            elevations = np.append(elevations, ele)

            for i in range(0, len(lon)):
                # Compute distance between with respect to 1st point
                d = distance.vincenty((lat0,lon0), (lat[i], lon[i])).kilometers
                distancevec.append(d)
                bearingvec.append(sphere.bearing((lat0,lon0), (lat[i], lon[i])))
        else:
            logger.debug("File is empty")
            os.remove(gpxfile)

    return distancevec, bearingvec, elevations

def make_pcolor_polar(figname, distancevec, bearingvec, rbins, thetabins, lon0, lat0, pointsInterest=None):
    """
    Create the plot showing how many times we've been in different subregions.
    """

    fig = plt.figure(figsize=(10, 10))
    ax = plt.subplot(111, projection='polar')
    # Histogramming
    ntheta = 16
    H, _, _ = np.histogram2d(distancevec, bearingvec, [rbins, thetabins])

    H = np.ma.masked_equal(H, 0., copy=True)

    # Plot
    Theta, R = np.meshgrid(thetabins, rbins)
    pcm = ax.pcolormesh(Theta, R, np.log10(H + 0.01), cmap=plt.cm.RdYlBu_r)
    lines, labels = plt.thetagrids( range(0,360,45), ('East', 'Northeast', 'North', 'Northwest',
                                                      'West','Southwest', 'South', 'Southeast') )

    lines, labels = plt.rgrids(np.arange(0., 6.1, 1.0),
                               ("", "1 km", "2 km", "3 km", "4 km", "5 km", "6 km" ),
                              angle=45. * 5/4. - 2.  )
    for ll in labels[1:]:
        ll.set_path_effects([PathEffects.withStroke(linewidth=2, foreground='w')])


    # Points of interest
    if pointsInterest is not None:
        for p in pointsInterest:
            bearing = np.deg2rad(sphere.bearing((lat0, lon0), (p[0], p[1])))
            dist = distance.vincenty((lat0, lon0), (p[0], p[1])).kilometers
            ax.text(bearing, dist, "\uf3c5", fontproperties=fp1,
             fontsize=14, ha="center", va="bottom", zorder=7)
            # ax.plot(bearing, dist, "ko")
            ax.text(bearing, dist, p[-1], ha="left", va="top")

    ax.plot((5 * np.pi/16., 5*np.pi/16.), (0.1, 6), 'k--')
    extax = ax.axes.spines['polar']
    #extax.set_visible(False)
    extax.set_linestyle("--")
    extax.set_color("0.7")
    # plt.colorbar(pcm)
    plt.savefig(figname, dpi=300, bbox_inches="tight")
    plt.close()


def main():
    basedir = "../data/"
    figdir = "../images/"
    figname = os.path.join(figdir, "GPX_polar12")

    logger = logging.getLogger("GPX_polar")
    logger.setLevel(logging.INFO)
    logging.info("starting")

    # Origin
    lon0, lat0, ele0 = 5.565, 50.582, 240.

    # Get the list of files
    filelist = []
    for yy in [2017, 2018, 2019,]:
        logger.debug("Year: {}".format(yy))
        gpxdir = "".join((basedir, str(yy)))
        filelist.extend(sorted(glob.glob(os.path.join(gpxdir, "*.gpx"))))
        logger.info(len(filelist))

    logger.info("Total number of files: {}".format(len(filelist)))

    # Compute distances and bearings
    distancevec, bearingvec, elevations = get_distance_bearing(filelist, lon0, lat0, logger)

    # Specify points of interest
    pointsInterest = [
        [50.552, 5.5502, "Roche aux Faucons"],
        [50.6024, 5.5957, "Lande de Streupas"],
        [50.5818, 5.6027, "Rochers du bout du monde"],
        [50.6007, 5.5554, "Point de vue"],
        [50.579064, 5.596830, "Chateau de Colonster"],
        [50.577784, 5.573265, "Piste\ndu Blanc Gravier"],
        ];

    # Bins for the plot
    bearingvec2 = np.deg2rad(bearingvec)
    rbins = np.arange(0, 6.01, 0.5)
    ntheta = 16.
    thetabins = np.linspace(0, 2*np.pi, ntheta + 1) + np.pi/ntheta

    # Make the plot
    logger.info("Creating the figure: {}".format(figname))
    make_pcolor_polar(figname, distancevec, bearingvec2, rbins, thetabins, lon0, lat0, pointsInterest)


if __name__ == "__main__":
    main()
