function isCompliantFourDigit(number) {
    /**
     * Determine whether a number is a compliant four-digit number
     * @param {number} number - The number to check.
     * @returns {boolean} True if the number is a compliant four-digit number, false otherwise.
     */

    // Check if the number is an integer and has exactly four digits
    return Number.isInteger(number) && number >= 1000 && number <= 9999;
}