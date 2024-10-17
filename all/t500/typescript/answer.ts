function convertScoreToDecimal(scoreStr: string): number | null {
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
        if (error instanceof Error) {
            console.error(`Error converting '${scoreStr}' to decimal: ${error.message}`);
        }
        return null;
    }
}