from math import sqrt

from numpy import NAN


def euclidean_dist(r1, r2):
    distance = 0
    allCount = len(r1)  # we assume both lists given are of equal length
    includedCount = 0
    for i in range(allCount):
        if r1[i] == r1[i] and r2[i] == r2[i]:
            includedCount += 1
            distance += (r1[i] - r2[i]) ** 2
    return sqrt(distance * (allCount / includedCount)) if includedCount != 0 else NAN
