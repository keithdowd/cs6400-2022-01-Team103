import math
#search for users within x miles

def haversine(latitude, longitude):
    #calculate distance between two points
    #latitude, longitude are expressed in degree
    #convert degrees to radians
    R = 6371e3
    converted_latitude = latitude * math.pi/180
    converted_longitude = longitude * math.pi/180

    a = ((math.sin*(converted_latitude/2))(math.sin(converted_longitude/2)) + math.cos(converted_latitude)(math.cos(converted_latitude*2))(math.sin(converted_longitude/2))(math.sin(converted_longitude/2)))
    c = (2 * a(math.tan(math.sqrt(a), math.sqrt(1-a))))
    d = R * c
    return d

#loop through all the distance until distance <=d
# loop through all zip code
# loop if zip code distance is <=D, return and put into search results