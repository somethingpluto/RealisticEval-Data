/**
 * Determine whether a number is a compliant four-digit number.
 *
 * @param {number} number - The number to check.
 * @returns {boolean} True if the number is a compliant four-digit number, false otherwise.
 */
function isCompliantFourDigit(number) {
    // Check if the number is an integer and within the range of 1000 to 9999
    return Number.isInteger(number) && number >= 1000 && number <= 9999;
}