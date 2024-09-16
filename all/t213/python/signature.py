import numpy as np

def im2col(image, filter_height, filter_width, stride=1, padding=0):
    """
    Apply the im2col operation to an input image.

    Parameters:
    - image (numpy array): The input image of shape (C, H, W) where:
        C: Number of channels
        H: Height of the image
        W: Width of the image
    - filter_height (int): Height of the filter
    - filter_width (int): Width of the filter
    - stride (int): Stride of the filter
    - padding (int): Number of pixels to pad the input image

    Returns:
    - col (numpy array): A 2D array where each column is a flattened filter region
    """