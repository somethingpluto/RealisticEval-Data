class SeededRandom:
    """
    Define a class called SeededRandom for generating pseudorandom numbers with a specific seed.
    """

    def __init__(self, seed):
        """
        Initializes a new instance of the SeededRandom class with a given seed.

        :param seed: The initial seed value for the random number generator.
        """

    def rand(self):
        """
        Generates a random number between 0 and 1 using a Linear Congruential Generator (LCG) algorithm.

        :returns: A pseudo-random number between 0 (inclusive) and 1 (exclusive).
        """
