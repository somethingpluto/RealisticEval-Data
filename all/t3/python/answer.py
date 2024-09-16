import math

import numpy as np
from PIL import Image


def crop_and_rotate_image(image_data, corner_points) -> np.ndarray:
    image = Image.fromarray(image_data)
    # Extract corner points for readability
    ul, ur, lr, ll = corner_points

    # Calculate width, height based on corner points
    width = int(np.linalg.norm(np.array(ur) - np.array(ul)))
    height = int(np.linalg.norm(np.array(ul) - np.array(ll)))

    # Calculate the center and the angle for rotation
    center_x = int((ul[0] + lr[0]) / 2)
    center_y = int((ul[1] + lr[1]) / 2)
    dx, dy = ur[0] - ul[0], ur[1] - ul[1]
    angle = math.degrees(math.atan2(dy, dx))

    # Rotate image to align the cropping area horizontally
    rotated = image.rotate(-angle, resample=Image.BICUBIC, center=(center_x, center_y))

    # Crop the aligned image
    left, upper = center_x - width // 2, center_y - height // 2
    cropped = rotated.crop((left, upper, left + width, upper + height))
    return np.array(cropped)
