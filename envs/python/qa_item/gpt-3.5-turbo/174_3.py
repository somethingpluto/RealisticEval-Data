from typing import Tuple
import math

def find_t_for_x(target_x: float, p0: Tuple[float, float], p1: Tuple[float, float], p2: Tuple[float, float]) -> float:
    def bezier(t: float, p0: float, p1: float, p2: float) -> float:
        return (1 - t) ** 2 * p0 + 2 * (1 - t) * t * p1 + t ** 2 * p2

    def bezier_derivative(t: float, p0: float, p1: float, p2: float) -> float:
        return 2 * (1 - t) * (p1 - p0) + 2 * t * (p2 - p1)
    
    def newton_raphson(target_x: float, p0: float, p1: float, p2: float) -> float:
        t = 0.5  # Initial guess
        epsilon = 1e-6
        
        while True:
            x = bezier(t, p0, p1, p2)
            dx = bezier_derivative(t, p0, p1, p2)
            t -= (x - target_x) / dx
            
            if abs(x - target_x) < epsilon:
                break
        
        return t
    
    return newton_raphson(target_x, p0[0], p1[0], p2[0])
import unittest

class TestFindxTForX(unittest.TestCase):
    TOLERANCE = 1e-6

    def test_find_t_for_x_at_start(self):
        p0 = 0.0
        p1 = 0.5
        p2 = 1.0
        target_x = 0.0
        t = find_t_for_x(target_x, p0, p1, p2)
        self.assertAlmostEqual(t, 0.0, delta=self.TOLERANCE)

    def test_find_t_for_x_at_end(self):
        p0 = 0.0
        p1 = 0.5
        p2 = 1.0
        target_x = 1.0
        t = find_t_for_x(target_x, p0, p1, p2)
        self.assertAlmostEqual(t, 1.0, delta=self.TOLERANCE)

    def test_find_t_for_x_mid_curve(self):
        p0 = 0.0
        p1 = 0.5
        p2 = 1.0
        target_x = 0.25
        t = find_t_for_x(target_x, p0, p1, p2)
        self.assertAlmostEqual(t, 0.25, delta=self.TOLERANCE)

    def test_find_t_for_x_near_mid_curve(self):
        p0 = 0.0
        p1 = 1.0
        p2 = 2.0
        target_x = 1.5
        t = find_t_for_x(target_x, p0, p1, p2)
        self.assertAlmostEqual(t, 0.75, delta=self.TOLERANCE)
if __name__ == '__main__':
    unittest.main()