from typing import Tuple
import numpy as np

class QuadratureRule:
    def __init__(self, x: np.ndarray, w: np.ndarray):
        self.x = x
        self.w = w

def lanczos(n: int, quadrature_rule: QuadratureRule) -> Tuple[np.ndarray, np.ndarray, np.ndarray, QuadratureRule]:
    """
    Implements the Lanczos function for the recursive relation coefficient algorithm for computing orthogonal polynomials.

    Args:
        n (int): The number of orthogonal polynomials to generate.
        quadrature_rule (QuadratureRule): An object containing x (nodes) and w (weights) for the quadrature.

    Returns:
        Tuple[np.ndarray, np.ndarray, np.ndarray, QuadratureRule]:
            - alpha: The diagonal elements of the tridiagonal matrix.
            - beta: The off-diagonal elements of the tridiagonal matrix.
            - p: The orthogonal polynomials.
            - quadrature_rule: The updated quadrature rule.
    """
    x = quadrature_rule.x
    w = quadrature_rule.w
    
    # Initialize arrays
    alpha = np.zeros(n)
    beta = np.zeros(n)
    p = np.zeros((n, len(x)))
    
    # Initial polynomial
    p[0, :] = 1.0
    
    # Compute the first alpha and beta
    alpha[0] = np.sum(w * x * p[0, :]**2) / np.sum(w * p[0, :]**2)
    beta[0] = np.sqrt(np.sum(w * p[0, :]**2))
    
    # Normalize the first polynomial
    p[0, :] /= beta[0]
    
    # Compute the rest of the polynomials
    for k in range(1, n):
        # Compute the next polynomial
        p[k, :] = (x - alpha[k-1]) * p[k-1, :] - beta[k-1] * p[k-2, :] if k > 1 else (x - alpha[k-1]) * p[k-1, :]
        
        # Compute alpha and beta
        alpha[k] = np.sum(w * x * p[k, :] * p[k-1, :]) / np.sum(w * p[k-1, :]**2)
        beta[k] = np.sum(w * p[k, :] * p[k-1, :]) / np.sum(w * p[k-1, :]**2)
        
        # Normalize the polynomial
        p[k, :] /= np.sqrt(np.sum(w * p[k, :]**2))
    
    # Update the quadrature rule with the new nodes and weights
    new_x = alpha
    new_w = beta[1:]**2
    
    quadrature_rule = QuadratureRule(new_x, new_w)
    
    return alpha, beta, p, quadrature_rule
import unittest

import numpy as np


class QuadratureRule:
    def __init__(self, x, w):
        self.x = np.array(x)
        self.w = np.array(w)


class TestOrthogonalPolynomial(unittest.TestCase):
    def test_lanczos_basic(self):
        x = [0.0, 0.5, 1.0]
        w = [0.333, 0.333, 0.334]
        quadrature_rule = QuadratureRule(x, w)
        n = 2
        alpha, beta, gamma, _ = lanczos(n, quadrature_rule)

        self.assertEqual(len(alpha), n)
        self.assertEqual(len(beta), n - 1)
        self.assertEqual(len(gamma), n)

    def test_lanczos_n_greater_than_length(self):
        x = [0.0, 0.5, 1.0]
        w = [0.333, 0.333, 0.334]
        quadrature_rule = QuadratureRule(x, w)
        n = 4

        with self.assertRaises(ValueError):
            lanczos(n, quadrature_rule)

    def test_lanczos_n_zero(self):
        x = [0.0, 0.5, 1.0]
        w = [0.333, 0.333, 0.334]
        quadrature_rule = QuadratureRule(x, w)
        n = 0

        with self.assertRaises(ValueError):
            lanczos(n, quadrature_rule)

    def test_lanczos_weights_nonuniform(self):
        x = [0.0, 0.5, 1.0]
        w = [0.1, 0.4, 0.5]
        quadrature_rule = QuadratureRule(x, w)
        n = 3
        alpha, beta, gamma, _ = lanczos(n, quadrature_rule)

        self.assertEqual(len(alpha), n)
        self.assertEqual(len(beta), n - 1)
        self.assertEqual(len(gamma), n)
        self.assertTrue(np.all(gamma > 0))

    def test_lanczos_single_node(self):
        x = [0.5]
        w = [1.0]
        quadrature_rule = QuadratureRule(x, w)
        n = 1
        alpha, beta, gamma, _ = lanczos(n, quadrature_rule)

        self.assertEqual(len(alpha), n)
        self.assertEqual(len(beta), n - 1)
        self.assertEqual(len(gamma), n)
        self.assertTrue(np.all(gamma > 0))
if __name__ == '__main__':
    unittest.main()