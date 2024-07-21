import math

import numpy as np
from PIL import Image


def rotatedCrop(img, corners):
    image = Image.fromarray(img)
    #code written by chatgpt4
    upper_left, upper_right, lower_right, lower_left = corners

    # Calculate the width and height of the unrotated box
    width = int(np.linalg.norm(np.array(upper_right) - np.array(upper_left)))
    height = int(np.linalg.norm(np.array(upper_left) - np.array(lower_left)))

    # Calculate the center of the box
    center_x = int((upper_left[0] + lower_right[0]) / 2)
    center_y = int((upper_left[1] + lower_right[1]) / 2)

    # Calculate the rotation angle of the box
    dx = upper_right[0] - upper_left[0]
    dy = upper_right[1] - upper_left[1]
    rotation_angle = math.degrees(math.atan2(dy, dx))

    # Rotate the image back by rotation_angle
    rotated_image = image.rotate(rotation_angle, resample=Image.BICUBIC, center=(center_x, center_y))

    # Crop the unrotated box
    left = center_x - width // 2
    upper = center_y - height // 2
    right = center_x + width // 2
    lower = center_y + height // 2
    cropped_image = rotated_image.crop((left, upper, right, lower))
    return np.array(cropped_image)