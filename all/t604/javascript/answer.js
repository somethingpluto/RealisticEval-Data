/**
 * Tail-recursive function to calculate x raised to the power y.
 *
 * This function uses tail recursion to compute x^y.
 *
 * @param {number} x The base, a non-negative integer.
 * @param {number} y The exponent, a non-negative integer.
 * @param {number} acc The accumulator to hold the intermediate result.
 *
 * @return {number} The result of x raised to the power of y.
 */
function powerTail(x, y, acc = 1) {
    // Base case: if exponent y is 0, return the accumulated result
    if (y === 0) {
        return acc;  // Return accumulated result
    }

    // Tail-recursive call with decremented exponent and updated accumulator
    return powerTail(x, y - 1, acc * x);
}