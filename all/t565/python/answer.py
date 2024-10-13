from typing import List, Dict

# Define the Coordinates type to represent a point in 2D space
Coordinates = Dict[str, float]


def get_bezier_point(t: float, points: List[Coordinates]) -> Coordinates:
    """
    Recursively calculates a point on a Bézier curve using De Casteljau's algorithm.

    Args:
        t: A value between 0 and 1 representing the interpolation parameter.
        points: A list of control points defining the Bézier curve.

    Returns:
        The calculated Coordinates at the given parameter t.
    """
    # If there's only one point, return it as the result
    if len(points) == 1:
        return points[0]

    # Create a list to hold the points for the next iteration
    next_points: List[Coordinates] = []

    # Calculate the intermediate points for the next iteration
    for i in range(len(points) - 1):
        x = (1 - t) * points[i]['x'] + t * points[i + 1]['x']
        y = (1 - t) * points[i]['y'] + t * points[i + 1]['y']
        next_points.append({'x': x, 'y': y})

    # Recursively call get_bezier_point with the new points
    return get_bezier_point(t, next_points)
