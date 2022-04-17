import math

# Returns miles
def haversine(lat1, lat2, long1, long2):
  R = 6371*1000
  lat1_conv = lat1*math.pi/180
  lat2_conv = lat2*math.pi/180
  chg_lat = (lat2-lat1)*math.pi/180
  chg_long = (long2-long1)*math.pi/180
  a=math.sin(chg_lat/2)*math.sin(chg_lat/2)+math.cos(lat1_conv)*math.cos(lat2_conv)*math.sin(chg_long/2)*math.sin(chg_long/2)
  c = (2 * (math.atan2(math.sqrt(a), math.sqrt(1-a))))
  d = (R * c) / 1000  # kilometers
  d = d *  0.62137 # miles
  return d