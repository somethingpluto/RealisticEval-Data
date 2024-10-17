#include <iostream>
#include <stdexcept>

// Function to perform modular exponentiation: (base^exponent) % modulus efficiently.
long long mod_exp(long long base, long long exponent, long long modulus) {
    if (modulus <= 0) {
        throw std::invalid_argument("Modulus must be a positive integer.");
    }

    long long result = 1;
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