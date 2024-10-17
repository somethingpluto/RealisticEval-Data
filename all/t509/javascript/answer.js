function modExp(base, exponent, modulus) {
    /**
     * Perform modular exponentiation: (base^exponent) % modulus efficiently.
     *
     * Parameters:
     * base (number): The base value.
     * exponent (number): The exponent value (should be non-negative).
     * modulus (number): The modulus value (should be positive).
     *
     * Returns:
     * number: The result of (base^exponent) % modulus.
     *
     * Throws:
     * Error: If modulus is less than or equal to zero.
     */

    if (modulus <= 0) {
        throw new Error("Modulus must be a positive integer.");
    }

    let result = 1;
    base = base % modulus;  // Ensure base is within the modulus

    while (exponent > 0) {
        // If exponent is odd, multiply the base with the result
        if (exponent % 2 === 1) {
            result = (result * base) % modulus;
        }

        // Right shift the exponent by 1 (equivalent to exponent >>= 1)
        exponent >>= 1;
        // Square the base
        base = (base * base) % modulus;
    }

    return result;
}