# Created by ChatGPT3 - For Use in a Refactor
import math


def haversine(lat1, lon1, lat2, lon2):
    R = 20_902_766  # radius of Earth in feet
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = (math.sin(dlat / 2) ** 2) + (math.cos(math.radians(lat1)) *
                                     math.cos(math.radians(lat2)) * (math.sin(dlon / 2) ** 2))
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c
