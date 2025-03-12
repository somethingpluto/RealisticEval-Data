/**
 * Perform modular exponentiation: (base^exponent) % modulus efficiently.
 *
 * @param {number} base - The base value.
 * @param {number} exponent - The exponent value (should be non-negative).
 * @param {number} modulus - The modulus value (should be positive).
 * @returns {number} The result of (base^exponent) % modulus.
 */
function modExp(base, exponent, modulus) {
    if (modulus === 1) return 0;

    let result = 1;
    base = base % modulus;

    while (exponent > 0) {
        // If exponent is odd, multiply base with result
        if (exponent % 2 === 1) {
            result = (result * base) % modulus;
        }

        // exponent must be even now
        exponent = exponent >> 1; // Divide exponent by 2
        base = (base * base) % modulus; // Square the base
    }

    return result;
}

