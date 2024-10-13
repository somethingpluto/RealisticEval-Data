def bezier(t: float, p0: float, p1: float, p2: float, p3: float) -> float:
    """
    Calculates the value of a cubic Bezier curve at a given parameter t.

    Args:
        t (float): The parameter value between 0 and 1 that represents a position along the curve.
        p0 (float): The first control point of the curve, typically where the curve starts.
        p1 (float): The second control point, which influences the tangent at the beginning of the curve.
        p2 (float): The third control point, which influences the tangent at the end of the curve.
        p3 (float): The fourth control point, typically where the curve ends.

    Returns:
        float: The point on the Bezier curve corresponding to the parameter t.
    """
