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
        if (exponent % 2 === 1) {
            result = (result * base) % modulus;
        }
        exponent = Math.floor(exponent / 2);
        base = (base * base) % modulus;
    }
    return result;
}

