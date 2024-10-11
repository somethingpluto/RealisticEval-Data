/**
 * Increments the entered number.
 * If the number is non-positive (<= 0), returns the original value.
 * If the number is positive, returns the value plus 1.
 *
 * @param {number} num - The number to increment.
 * @returns {number} - The incremented value or the original number.
 */
function incrementNumber(num) {
    if (num > 0) {
        return num + 1; // Increment if positive
    }
    return num; // Return original value if non-positive
}
