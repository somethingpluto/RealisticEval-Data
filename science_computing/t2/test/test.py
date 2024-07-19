import unittest
import numpy as np
from PIL import Image

from task_code.t7.adapted import rotate_and_crop


class TestRotateAndCrop(unittest.TestCase):

    def test_rotate_and_crop(self):
        # Create a dummy image (100x100 white square with a black border)
        img = np.ones((100, 100, 3), dtype=np.uint8) * 255
        img[:, 0] = 0
        img[:, -1] = 0
        img[0, :] = 0
        img[-1, :] = 0

        # Define corners of a 50x50 square in the center, rotated 45 degrees
        corners = [(35, 35), (65, 35), (65, 65), (35, 65)]

        # Call the function
        cropped_image = rotate_and_crop(img, corners)

        # Convert result to PIL Image for inspection
        cropped_pil = Image.fromarray(cropped_image)

        # Check size of the cropped image
        self.assertEqual(cropped_pil.size, (50, 50))

        # Check that the center of the image is white
        center_pixel = cropped_image[25, 25]
        self.assertTrue(np.array_equal(center_pixel, [255, 255, 255]))

    def test_non_square_crop(self):
        # Create a dummy image (100x100 white square with a black border)
        img = np.ones((100, 100, 3), dtype=np.uint8) * 255
        img[:, 0] = 0
        img[:, -1] = 0
        img[0, :] = 0
        img[-1, :] = 0

        # Define corners of a 40x60 rectangle in the center, rotated 30 degrees
        corners = [(40, 30), (60, 30), (70, 60), (50, 60)]

        # Call the function
        cropped_image = rotate_and_crop(img, corners)

        # Convert result to PIL Image for inspection
        cropped_pil = Image.fromarray(cropped_image)

        # Check size of the cropped image
        self.assertEqual(cropped_pil.size, (50, 40))

        # Check that the center of the image is white
        center_pixel = cropped_image[20, 25]
        self.assertTrue(np.array_equal(center_pixel, [255, 255, 255]))

    def test_large_rotation(self):
        # Create a dummy image (100x100 white square with a black border)
        img = np.ones((100, 100, 3), dtype=np.uint8) * 255
        img[:, 0] = 0
        img[:, -1] = 0
        img[0, :] = 0
        img[-1, :] = 0

        # Define corners of a 50x50 square in the center, rotated 90 degrees
        corners = [(25, 25), (75, 25), (75, 75), (25, 75)]

        # Call the function
        cropped_image = rotate_and_crop(img, corners)

        # Convert result to PIL Image for inspection
        cropped_pil = Image.fromarray(cropped_image)

        # Check size of the cropped image
        self.assertEqual(cropped_pil.size, (50, 50))

        # Check that the center of the image is white
        center_pixel = cropped_image[25, 25]
        self.assertTrue(np.array_equal(center_pixel, [255, 255, 255]))
