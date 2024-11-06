function sumCalibrationValues(calibrationDocument: string[]): number {
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