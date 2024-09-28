# Created with GPT-4 #
def point_inside(self, point: tuple[float, float]) -> bool:
    """
    Check if a given point is inside the triangle.

    :param point: A tuple (x, y) representing the point to check.
    :type point: tuple[float, float]

    :return: True if the point is inside the triangle, False otherwise.
    :rtype: bool
    """

    def sign(p1: tuple[float, float], p2: tuple[float, float], p3: tuple[float, float]) -> float:
        return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])

    b1: bool = sign(point, self.points[0], self.points[1]) < 0.0
    b2: bool = sign(point, self.points[1], self.points[2]) < 0.0
    b3: bool = sign(point, self.points[2], self.points[0]) < 0.0

    return (b1 == b2) and (b2 == b3)