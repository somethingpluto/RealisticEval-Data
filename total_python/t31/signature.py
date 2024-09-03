from typing import List, Tuple


def calculate_red_proportion(pixels: List[Tuple[int, int, int]]) -> float:
    """
    Analyze a list of pixels, each represented by rgb, and calculate the proportion of red in the list.

    Args:
        pixels (List[Tuple[int, int, int]]): A list of pixels, where each pixel is represented as a tuple of (R, G, B).

    Returns:
        float: The proportion of red in the list of pixels, as a value between 0 and 1.
    """