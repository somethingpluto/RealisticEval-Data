import math

class SeededRandom:
    def __init__(self, seed):
        self.a = 16807
        self.c = 0
        self.m = 2**31
        self.x = int(seed)

    def rand(self):
        self.x = (self.a * self.x + self.c) % self.m
        if self.x <= (self.m // 2):
            self.x = self.x + self.m
        return float(self.x) / self.m
import unittest


class TestSeededRandom(unittest.TestCase):

    def test_consistent_numbers_with_same_seed(self):
        """Generates consistent numbers with the same seed."""
        seeded_rand1 = SeededRandom(42)
        seeded_rand2 = SeededRandom(42)
        self.assertAlmostEqual(seeded_rand1.rand(), seeded_rand2.rand(), places=10)
        self.assertAlmostEqual(seeded_rand1.rand(), seeded_rand2.rand(), places=10)
        self.assertAlmostEqual(seeded_rand1.rand(), seeded_rand2.rand(), places=10)

    def test_different_numbers_with_different_seeds(self):
        """Generates different numbers with different seeds."""
        seeded_rand1 = SeededRandom(42)
        seeded_rand2 = SeededRandom(24)
        self.assertNotAlmostEqual(seeded_rand1.rand(), seeded_rand2.rand(), places=10)

    def test_returns_numbers_between_0_and_1(self):
        """Returns numbers between 0 and 1."""
        seeded_rand = SeededRandom(123456)
        for _ in range(1000):
            rand_value = seeded_rand.rand()
            self.assertGreaterEqual(rand_value, 0)
            self.assertLess(rand_value, 1)

    def test_different_sequences_with_different_seeds(self):
        """Produces different sequences with different seeds."""
        seeded_rand1 = SeededRandom(123)
        seeded_rand2 = SeededRandom(456)
        sequence1 = [seeded_rand1.rand() for _ in range(5)]
        sequence2 = [seeded_rand2.rand() for _ in range(5)]
        self.assertNotEqual(sequence1, sequence2)

    def test_consistent_sequence_with_same_seed(self):
        """Consistent sequence with the same seed over multiple calls."""
        seeded_rand = SeededRandom(987654321)
        sequence1 = [seeded_rand.rand() for _ in range(3)]
        seeded_rand2 = SeededRandom(987654321)
        sequence2 = [seeded_rand2.rand() for _ in range(3)]
        self.assertEqual(sequence1, sequence2)

if __name__ == '__main__':
    unittest.main()