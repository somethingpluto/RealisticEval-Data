def cubic_bezier(t: float, p0: list, p1: list, p2: list, p3: list) -> list:
    """
    Calculate the coordinates of a cubic Bézier curve at a given parameter t (typically between 0 and 1).

    Args:
        t (float): A float representing the parameter along the curve, where 0 <= t <= 1.
        p0 (list): A list of size 2 representing the x and y coordinates of the start point.
        p1 (list): A list of size 2 representing the x and y coordinates of the first control point.
        p2 (list): A list of size 2 representing the x and y coordinates of the second control point.
        p3 (list): A list of size 2 representing the x and y coordinates of the end point.

    Returns:
        list: A list of size 2 containing the x and y coordinates of the point on the curve corresponding to the parameter t.
    """