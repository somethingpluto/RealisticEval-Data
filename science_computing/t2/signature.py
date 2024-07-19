from typing import List, Tuple
import numpy as np
import math
from PIL import Image


def rotate_and_crop(img: np.ndarray, corners: List[Tuple[int, int]]) -> np.ndarray:
    """
    Rotate and crop an image based on the given corners of a rotated rectangle.

    Args:
        img (np.ndarray): The input image.
        corners (List[Tuple[int, int]]): A list of four corners (upper-left, upper-right, lower-right, lower-left).

    Returns:
        np.ndarray: The cropped image.
    """