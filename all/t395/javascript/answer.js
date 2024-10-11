function sumCalibrationValues(calibrationDocument) {
    /**
     * Sums up calibration values extracted from the document.
     * Each calibration value is formed by combining the first and last digits of numbers found in each line
     * into a two-digit number.
     *
     * @param {string[]} calibrationDocument - An array of strings, each representing a line of text.
     * @returns {number} - The total sum of all calibration values.
     */

    let sum = 0;

    calibrationDocument.forEach(line => {
        const matches = line.match(/\d+/g);
        if (matches && matches.length > 0) {
            matches.forEach(match => {
                const num = parseInt(match[0] + match[match.length - 1], 10);
                sum += num;
            });
        }
    });

    return sum;
}