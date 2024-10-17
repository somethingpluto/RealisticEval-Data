function convertScoreToDecimal(scoreStr) {
    /**
     * Converts the string representation of a score to its decimal value.
     *
     * @param {string} scoreStr - The score as a string, can be a decimal or a fraction (e.g., "2.5", "10/4")
     * @returns {number | null} - The decimal value of the score as a float, or null if the input is invalid
     */
    try {
        // Check if the score is a fraction
        if (scoreStr.includes('/')) {
            const [numerator, denominator] = scoreStr.split('/');
            const decimalValue = parseFloat(numerator) / parseFloat(denominator);
            return decimalValue;
        } else {
            // Otherwise, treat it as a decimal
            const decimalValue = parseFloat(scoreStr);
            return decimalValue;
        }

    } catch (error) {
        console.log(`Error converting '${scoreStr}' to decimal: ${error.message}`);
        return null;
    }
}