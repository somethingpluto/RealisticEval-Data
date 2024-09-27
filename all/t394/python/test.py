import unittest


class TestGradientDescentEuclidean(unittest.TestCase):

    def test_convergence_to_minimum(self):
        """ Test that gradient descent converges to the minimum of f(x) = (x-3)^2 """

        def grad_f(x):
            return 2 * (x - 3)  # Gradient of f(x) = (x - 3)^2

        start = 0.0
        learning_rate = 0.1
        n_steps = 30

        path = gradient_descent_euclidean(start, learning_rate, n_steps, grad_f)
        final_position = path[-1]

        self.assertAlmostEqual(final_position, 3.0, delta=0.1)  # Check that we are near the minimum

    def test_no_steps(self):
        """ Test the case where no steps are taken. """

        def grad_f(x):
            return 2 * (x - 3)

        start = 0.0
        learning_rate = 0.1
        n_steps = 0

        path = gradient_descent_euclidean(start, learning_rate, n_steps, grad_f)

        self.assertEqual(path.shape[0], 1)  # Only the start point should be returned
        self.assertAlmostEqual(path[0], start)

    def test_large_learning_rate(self):
        """ Test with a large learning rate, which may overshoot the minimum. """

        def grad_f(x):
            return 2 * (x - 3)

        start = 0.0
        learning_rate = 1.0  # Large learning rate
        n_steps = 10

        path = gradient_descent_euclidean(start, learning_rate, n_steps, grad_f)

        # Check that the last position is not too close to the expected minimum
        self.assertNotAlmostEqual(path[-1], 3.0, delta=0.5)


    def test_path_length(self):
        """ Test that the path length is correct. """

        def grad_f(x):
            return 2 * (x - 3)

        start = 0.0
        learning_rate = 0.1
        n_steps = 20

        path = gradient_descent_euclidean(start, learning_rate, n_steps, grad_f)

        self.assertEqual(len(path), n_steps + 1)  # +1 for the initial point