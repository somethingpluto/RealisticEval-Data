import math
import unittest

from total.t4.adapted import quaternion_to_yaw


class TestQuaternionToYaw(unittest.TestCase):
    def test_zero_rotation(self):
        self.assertAlmostEqual(quaternion_to_yaw(0, 0, 0, 1), 0)

    def test_half_pi_rotation(self):
        self.assertAlmostEqual(quaternion_to_yaw(0, 0, 1, 0), math.pi)

    def test_quarter_pi_rotation(self):
        self.assertAlmostEqual(quaternion_to_yaw(0, 0, 0.7071, 0.7071), math.pi / 2)