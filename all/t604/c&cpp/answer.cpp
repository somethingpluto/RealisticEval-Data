#include <iostream>

/**
 * @brief Tail-recursive function to calculate x raised to the power y.
 *
 * This function uses tail recursion to compute x^y.
 *
 * @param x The base, a non-negative integer.
 * @param y The exponent, a non-negative integer.
 * @param acc The accumulator to hold the intermediate result.
 *
 * @return The result of x raised to the power of y.
 */
unsigned power_tail(unsigned x, unsigned y, unsigned acc = 1) {
    // Base case: if exponent y is 0, return the accumulated result
    if (y == 0) {
        return acc;  // Return accumulated result
    }

    // Tail-recursive call with decremented exponent and updated accumulator
    return power_tail(x, y - 1, acc * x);
}