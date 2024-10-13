def get_bezier_point(t: float, points: list[Coordinates]) -> Coordinates:
    """
    Recursively calculates a point on a Bézier curve using De Casteljau's algorithm.

    Args:
        t: A value between 0 and 1 representing the interpolation parameter.
        points: A list of control points defining the Bézier curve.

    Returns:
        The calculated Coordinates at the given parameter t.
    """