def intersect_vertically(rect1, rect2):
    return not (rect1[3] < rect2[1] or rect2[3] < rect1[1])
