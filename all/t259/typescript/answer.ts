function isCompliantFourDigit(number: number): boolean {
    /**
     * Determine whether a number is a compliant four-digit number
     * @param {number} number - The number to check.
     * @returns {boolean} True if the number is a compliant four-digit number, false otherwise.
     */
    return number >= 1000 && number <= 9999;
}