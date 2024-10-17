package org.real.temp;

public class Answer {

    /**
     * Perform modular exponentiation: (base^exponent) % modulus efficiently.
     *
     * @param base     The base value.
     * @param exponent The exponent value (should be non-negative).
     * @param modulus  The modulus value (should be positive).
     * @return The result of (base^exponent) % modulus.
     * @throws IllegalArgumentException If modulus is less than or equal to zero.
     */
    public static int modExp(int base, int exponent, int modulus) {
        if (modulus <= 0) {
            throw new IllegalArgumentException("Modulus must be a positive integer.");
        }

        int result = 1;
        base = base % modulus;  // Ensure base is within the modulus

        while (exponent > 0) {
            // If exponent is odd, multiply the base with the result
            if (exponent % 2 == 1) {
                result = (result * base) % modulus;
            }

            // Right shift the exponent by 1 (equivalent to exponent //= 2)
            exponent >>= 1;
            // Square the base
            base = (base * base) % modulus;
        }

        return result;
    }

    public static void main(String[] args) {
        // Example usage
        System.out.println(modExp(2, 3, 5));  // Output: 3
        System.out.println(modExp(7, 4, 13)); // Output: 9
    }
}