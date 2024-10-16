from typing import Dict, List


def calculate_toroidal_difference(point_a: Dict[str, float], point_b: Dict[str, float], width: float, height: float) -> List[float]:
    """
    Calculates the toroidal difference between two points in a wrap-around space.

    Args:
        point_a (Dict[str, float]): The first point with keys 'x' and 'y'.
        point_b (Dict[str, float]): The second point with keys 'x' and 'y'.
        width (float): The width of the toroidal space.
        height (float): The height of the toroidal space.

    Returns:
        List[float]: A list containing the x and y differences, accounting for wrap-around.
    """