

METADATA = {}


def check(candidate):
    assert candidate(5, 3) == 7.5
    assert candidate(2, 2) == 2.0
    assert candidate(10, 8) == 40.0

def triangle_area(base, height):
    """Given length of base and height return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    """
    return 0.5 * base * height
candidate = triangle_area
check(candidate)