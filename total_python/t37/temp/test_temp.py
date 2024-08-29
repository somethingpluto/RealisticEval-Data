import unittest

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
import numpy as np


class OrthogonalPolynomial:
    def __init__(self, alpha, beta, gamma, quadrature_rule):
        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma
        self.quadrature_rule = quadrature_rule


def lanczos(n, quadrature_rule):
    if n <= 0 or n > len(quadrature_rule.x):
        raise ValueError('n must be between 1 and len(x).')

    x = quadrature_rule.x
    w = quadrature_rule.w
    alpha = np.zeros(n)
    beta = np.zeros(n - 1) if n > 1 else np.array([])
    gamma = np.zeros(n)

    # Initial polynomial p_0(x) = 1, p_-1(x) = 0 (non-existent, thus ignored in calculations)
    p0 = np.ones(len(x))
    p1 = np.zeros(len(x))

    for i in range(n):
        # Compute new polynomial p_i
        pi = (x - alpha[i - 1]) * p0 if i > 0 else p0 - beta[i - 1] * p1 if i > 1 else p0
        gamma[i] = np.dot(w * pi, pi)
        alpha[i] = np.dot(w * x * pi, pi) / gamma[i]

        if i < n - 1:
            beta[i] = np.dot(w * pi * pi, pi) / gamma[i]
            p1, p0 = p0, pi  # Update polynomials for next iteration

    return alpha, beta, gamma, quadrature_rule
