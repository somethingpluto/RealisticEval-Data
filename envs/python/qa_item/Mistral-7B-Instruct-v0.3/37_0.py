import numpy as np
from typing import Tuple

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
            p (np.ndarray): array of orthogonal polynomials
            c (np.ndarray): array of recurrence coefficients
            norms (np.ndarray): array of norms of orthogonal polynomials
            updated_quadrature_rule (QuadratureRule): updated quadrature rule with new nodes and weights
    """

    p = np.zeros((n, len(quadrature_rule.x)))
    c = np.zeros(n)
    norms = np.zeros(n)
    updated_quadrature_rule = quadrature_rule

    for i in range(n):
        q = np.prod(quadrature_rule.x ** np.arange(i), axis=1)
        p[i] = q

        for j in range(i):
            p[i] -= c[j] * p[j]

        norms[i] = np.sqrt(np.dot(p[i], np.multiply(p[i], quadrature_rule.w)))
        c[i] = np.dot(p[i], np.multiply(quadrature_rule.x, p[i], axis=1)) / norms[i]

        # Update the quadrature rule with new nodes and weights
        new_x = np.append(quadrature_rule.x, np.zeros(1))
        new_w = np.append(np.zeros(len(quadrature_rule.x)), 2 * c[i])
        updated_quadrature_rule = QuadratureRule(new_x, new_w)

    return p, c, norms, updated_quadrature_rule
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