from typing import List, Dict


def get_bezier_point(t: float, points: List[Dict[str, float]]) -> Dict[str, float]:
    """
    Recursively calculates a point on a Bézier curve using De Casteljau's algorithm.

    Args:
        t(float): A value between 0 and 1 representing the interpolation parameter.
        points(List[Dict[str, float]]): A list of control points defining the Bézier curve.

    Returns:
        The calculated Coordinates at the given parameter t.
    """
