function sumCalibrationValues(calibrationDocument: string[]): number {
    /**
     * Sums up calibration values extracted from the document.
     * Each calibration value is formed by combining the first and last digits of numbers found in each line
     * into a two-digit number.
     *
     * @param {string[]} calibrationDocument - An array of strings, each representing a line of text.
     * @returns {number} The total sum of all calibration values.
     */
    
    let totalSum = 0;

    for (const line of calibrationDocument) {
        const matches = line.match(/\d+/g); // Find all sequences of digits

        if (matches) {
            for (const match of matches) {
                const firstDigit = parseInt(match[0], 10);
                const lastDigit = parseInt(match[match.length - 1], 10);

                if (!isNaN(firstDigit) && !isNaN(lastDigit)) {
                    totalSum += firstDigit * 10 + lastDigit;
                }
            }
        }
    }

    return totalSum;
}