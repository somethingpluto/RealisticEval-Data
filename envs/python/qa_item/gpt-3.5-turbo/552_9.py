import numpy as np

def are_sets_equal(set1, set2, rtol=1e-5, atol=1e-6):
    """
    Compares two sets of floats for equality within a relative and absolute tolerance.

    Args:
        set1: The first set of floats.
        set2: The second set of floats.
        rtol: The relative tolerance (default: 1e-5).
        atol: The absolute tolerance (default: 1e-6).

    Returns:
        True if the sets are equal within the specified tolerances, False otherwise.
    """
    return np.allclose(set1, set2, rtol=rtol, atol=atol)
import unittest


class TestAreSetsEqual(unittest.TestCase):

    def test_identical_sets(self):
        """Test with two identical sets of floats."""
        set1 = {1.0, 2.0, 3.0}
        set2 = {1.0, 2.0, 3.0}
        self.assertTrue(are_sets_equal(set1, set2))

    def test_sets_with_close_values(self):
        """Test with two sets that are close within the tolerance."""
        set1 = {1.0, 2.00001, 3.0}
        set2 = {1.0, 2.00002, 3.0}
        self.assertTrue(are_sets_equal(set1, set2, rtol=1e-5, atol=1e-6))

    def test_sets_with_large_difference(self):
        """Test with two sets that have large differences beyond tolerance."""
        set1 = {1.0, 2.0, 3.0}
        set2 = {1.0, 2.5, 3.0}
        self.assertFalse(are_sets_equal(set1, set2))

    def test_sets_with_one_different_values(self):
        """Test with two sets containing one different floats."""
        set1 = {1.0, 2.0, 3.0}
        set2 = {1.0, 2.000001, 3.0}
        self.assertTrue(are_sets_equal(set1, set2, rtol=1e-5, atol=1e-6))

    def test_empty_sets(self):
        """Test with two empty sets."""
        set1 = set()
        set2 = set()
        self.assertTrue(are_sets_equal(set1, set2))

if __name__ == '__main__':
    unittest.main()