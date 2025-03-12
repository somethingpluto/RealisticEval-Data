import numpy as np

def get_rotation(matrix:np.array) -> float:
    det = np.linalg.det(matrix)
    if det == 0:
        return 0.0
    
    scale_x = np.linalg.norm(matrix[:,0])
    scale_y = np.linalg.norm(matrix[:,1])
    
    sin_theta = det / (scale_x * scale_y)
    cos_theta = np.trace(matrix) / (2 * scale_x * scale_y)
    
    return np.arctan2(sin_theta, cos_theta)
import numpy as np
import unittest


class TestGetRotationFunction(unittest.TestCase):

    def test_rotation_0_degrees(self):
        """ Test for a rotation of 0 degrees (identity matrix) """
        matrix = np.array([[1, 0, 0],
                           [0, 1, 0],
                           [0, 0, 1]])
        expected_rotation = 0.0
        self.assertAlmostEqual(get_rotation(matrix), expected_rotation, places=6)

    def test_rotation_90_degrees(self):
        """ Test for a rotation of 90 degrees """
        matrix = np.array([[0, -1, 0],
                           [1, 0, 0],
                           [0, 0, 1]])
        expected_rotation = np.pi / 2  # 90 degrees in radians
        self.assertAlmostEqual(get_rotation(matrix), expected_rotation, places=6)

    def test_rotation_180_degrees(self):
        """ Test for a rotation of 180 degrees """
        matrix = np.array([[-1, 0, 0],
                           [0, -1, 0],
                           [0, 0, 1]])
        expected_rotation = np.pi  # 180 degrees in radians
        self.assertAlmostEqual(get_rotation(matrix), expected_rotation, places=6)

    def test_rotation_negative_90_degrees(self):
        """ Test for a rotation of -90 degrees """
        matrix = np.array([[0, 1, 0],
                           [-1, 0, 0],
                           [0, 0, 1]])
        expected_rotation = -np.pi / 2  # -90 degrees in radians
        self.assertAlmostEqual(get_rotation(matrix), expected_rotation, places=6)

if __name__ == '__main__':
    unittest.main()