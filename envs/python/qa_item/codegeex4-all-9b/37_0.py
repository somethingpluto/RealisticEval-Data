from typing import Tuple
import numpy as np

class QuadratureRule:
    def __init__(self, x: np.ndarray, w: np.ndarray):
        self.x = x
        self.w = w

def lanczos(n: int, quadrature_rule: QuadratureRule) -> Tuple[np.ndarray, np.ndarray, np.ndarray, QuadratureRule]:
    """
    implements the Lanczos function for the recursive relation coefficient algorithm for computing orthogonal polynomials
    Args:
        n (int): the number of orthogonal polynomials to generate
        quadrature_rule (QuadratureRule): An object containing x (nodes) and w (weights) for the quadrature.
    Returns:
        Tuple[np.ndarray, np.ndarray, np.ndarray, QuadratureRule]:
    """
    x = quadrature_rule.x
    w = quadrature_rule.w
    p = np.zeros((n, len(x)))
    p[0] = np.ones(len(x))
    alpha = np.zeros(n)
    beta = np.zeros(n)
    alpha[0] = 0.5 / (x[0] * x[0])
    for i in range(1, n):
        b = 0.0
        for j in range(i):
            b += alpha[j] * p[j] * p[i-1]
        b = 0.5 / (x[i] * x[i] - b)
        alpha[i] = b * x[i]
        beta[i] = -b
        for j in range(i):
            p[i] += alpha[j] * p[j] * p[i-1] - beta[j] * p[j-1] * p[i-2]
        p[i] *= w
    return p, alpha, beta, quadrature_rule
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