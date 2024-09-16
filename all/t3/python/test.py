import unittest
import numpy as np


class TestCropAndRotateImage(unittest.TestCase):
    def test_simple_rotation(self):
        # Create a blank image
        img = np.zeros((100, 100, 3), dtype=np.uint8)
        # Define corners of a central square, no rotation
        corners = [(30, 30), (70, 30), (70, 70), (30, 70)]
        # Expected to crop without rotation
        result = crop_and_rotate_image(img, corners)
        self.assertEqual(result.shape, (40, 40, 3))  # Check the dimensions of the output

    def test_rotation_and_crop(self):
        # Test with an actual image and rotation
        img = np.random.randint(0, 256, (100, 100, 3), dtype=np.uint8)
        # Corners rotated about 45 degrees
        corners = [(50, 30), (70, 50), (50, 70), (30, 50)]
        result = crop_and_rotate_image(img, corners)
        self.assertEqual(result.shape, (28, 28, 3))  # Approximately square output