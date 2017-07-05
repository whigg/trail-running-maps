import re

def read_gpx(filename):
    coords = []
    with open(filename) as f:
        for lines in f:
            match = re.search('<trkpt lat="([-0-9\.]+)" lon="([-0-9\.]+)">', lines)
            if match:
                coords.append((float(match.group(1)), float(match.group(2))))
    return coords
    
def read_gpx_lonlat(filename):
    lon, lat, elevation = [], [], []
    with open(filename) as f:
        for lines in f:
            match = re.search('<trkpt lat="([-0-9\.]+)" lon="([-0-9\.]+)">', lines)
            if match:
                lat.append(float(match.group(1)))
                lon.append(float(match.group(2)))
            else:
                matchele = re.search("<ele>([-0-9\.]+)</ele>", lines)
                if matchele:
                    elevation.append(float(matchele.group(1)))
              
    return lon, lat, elevation
   
