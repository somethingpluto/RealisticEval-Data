package org.real.temp;

/**
 * Define a class called SeededRandom for generating pseudorandom numbers with a specific seed.
 */
public class Answer {
    private long seed;

    /**
     * Initializes a new instance of the SeededRandom class with a given seed.
     * @param seed The initial seed value for the random number generator.
     */
    public SeededRandom(long seed) {
        this.seed = seed;
    }

    /**
     * Generates a random number between 0 and 1 using a Linear Congruential Generator (LCG) algorithm.
     * @return A pseudo-random number between 0 (inclusive) and 1 (exclusive).
     */
    public double rand() {
        // LCG parameters
        final long multiplier = 1664525;     // Multiplier value for the LCG
        final long increment = 1013904223;   // Increment value for the LCG
        final long modulus = (1L << 32);      // Modulus value (2^32) for the LCG

        // Update the seed using the LCG formula
        seed = (multiplier * seed + increment) % modulus;

        // Normalize the seed to a value between 0 and 1
        return (double) seed / modulus;
    }

    public static void main(String[] args) {
        SeededRandom random = new SeededRandom(12345);
        System.out.println(random.rand()); // Example usage
    }
}