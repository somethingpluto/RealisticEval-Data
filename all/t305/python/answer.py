class SeededRandom:
    """
    A class for generating pseudorandom numbers with a specific seed.
    """

    def __init__(self, seed):
        """
        Initializes a new instance of the SeededRandom class with a given seed.

        :param seed: The initial seed value for the random number generator.
        """
        self.seed = seed

    def rand(self):
        """
        Generates a random number between 0 and 1 using a Linear Congruential Generator (LCG) algorithm.

        :return: A pseudo-random number between 0 (inclusive) and 1 (exclusive).
        """
        # LCG parameters
        multiplier = 1664525  # Multiplier value for the LCG
        increment = 1013904223  # Increment value for the LCG
        modulus = 2 ** 32  # Modulus value (2^32) for the LCG

        # Update the seed using the LCG formula
        self.seed = (multiplier * self.seed + increment) % modulus

        # Normalize the seed to a value between 0 and 1
        return self.seed / modulus