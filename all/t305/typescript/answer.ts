/**
 * Define a class called SeededRandom for generating pseudorandom numbers with a specific seed
 */
class SeededRandom {
    private seed: number;

    /**
     * Initializes a new instance of the SeededRandom class with a given seed.
     * @param seed - The initial seed value for the random number generator.
     */
    constructor(seed: number) {
        this.seed = seed;
    }

    /**
     * Generates a random number between 0 and 1 using a Linear Congruential Generator (LCG) algorithm.
     * @returns A pseudo-random number between 0 (inclusive) and 1 (exclusive).
     */
    rand(): number {
        // LCG parameters
        const multiplier = 1664525;     // Multiplier value for the LCG
        const increment = 1013904223;   // Increment value for the LCG
        const modulus = 2 ** 32;        // Modulus value (2^32) for the LCG

        // Update the seed using the LCG formula
        this.seed = (multiplier * this.seed + increment) % modulus;

        // Normalize the seed to a value between 0 and 1
        return this.seed / modulus;
    }
}