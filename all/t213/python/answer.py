import unittest
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
    C, H, W = image.shape
    out_height = (H + 2 * padding - filter_height) // stride + 1
    out_width = (W + 2 * padding - filter_width) // stride + 1

    # Apply padding to the image
    padded_image = np.pad(image, ((0, 0), (padding, padding), (padding, padding)), mode='constant')

    # Initialize the column matrix
    col = np.zeros((C * filter_height * filter_width, out_height * out_width))

    # Fill the column matrix
    col_idx = 0
    for y in range(0, H + 2 * padding - filter_height + 1, stride):
        for x in range(0, W + 2 * padding - filter_width + 1, stride):
            patch = padded_image[:, y:y + filter_height, x:x + filter_width]
            col[:, col_idx] = patch.flatten()
            col_idx += 1

    return col