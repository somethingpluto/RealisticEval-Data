from typing import Tuple
import numpy as np

def find_t_for_x(target_x: float, p0: Tuple[float, float], p1: Tuple[float, float], p2: Tuple[float, float]) -> float:
    """
    Find the parameter t corresponding to a given x-coordinate target_x
    on a quadratic Bézier curve defined by control points p0, p1, and p2.

    Args:
        target_x (float): The x-coordinate for which we want to find the corresponding parameter t.
        p0 (Tuple[float, float]): The first control point of the Bézier curve.
        p1 (Tuple[float, float]): The second control point of the Bézier curve.
        p2 (Tuple[float, float]): The third control point of the Bézier curve.

    Returns:
        float: The parameter t (in the range [0, 1]) for which the Bézier curve evaluated at t is closest to target_x.
    """
    
    # Extract x-coordinates of control points
    x0, _ = p0
    x1, _ = p1
    x2, _ = p2
    
    # Define the quadratic Bézier curve function for x
    def bezier_x(t):
        return (1 - t)**2 * x0 + 2 * (1 - t) * t * x1 + t**2 * x2
    
    # Define the derivative of the quadratic Bézier curve function for x
    def bezier_x_derivative(t):
        return 2 * (1 - t) * (x1 - x0) + 2 * t * (x2 - x1)
    
    # Initial guess for t
    t = 0.5
    
    # Tolerance for convergence
    tolerance = 1e-6
    
    # Maximum number of iterations
    max_iterations = 100
    
    # Newton-Raphson method to find t
    for _ in range(max_iterations):
        fx = bezier_x(t) - target_x
        fpx = bezier_x_derivative(t)
        
        if abs(fx) < tolerance:
            break
        
        t = t - fx / fpx
        
        # Ensure t stays within [0, 1]
        t = max(0, min(1, t))
    
    return t
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