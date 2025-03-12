/**
 * Check for ticker symbols with the same ex-dividend date but different dividend amounts.
 * @param {Array} records - An array of arrays, where each inner array contains [ticker, exDividendDate, dividendAmount].
 * @returns {Array} An array of arrays, where each inner array contains [ticker, exDividendDate] that have different dividend amounts.
 */
function checkDividendVariances(records) {
    // Create a map to store ex-dividend dates and their corresponding dividend amounts
    const exDividendMap = new Map();

    // Iterate through each record
    for (const [ticker, exDividendDate, dividendAmount] of records) {
        // Create a unique key for the ex-dividend date
        const key = `${ticker}-${exDividendDate}`;

        // If the key already exists in the map, check if the dividend amount is different
        if (exDividendMap.has(key)) {
            const existingAmount = exDividendMap.get(key);
            if (existingAmount !== dividendAmount) {
                // If different, store the key in the map with the new amount
                exDividendMap.set(key, null); // Use null to indicate variance
            }
        } else {
            // If the key does not exist, store the dividend amount
            exDividendMap.set(key, dividendAmount);
        }
    }

    // Filter out the keys that have variances
    const result = [];
    for (const [key, amount] of exDividendMap.entries()) {
        if (amount === null) {
            // Extract the ticker and ex-dividend date from the key
            const [ticker, exDividendDate] = key.split('-');
            result.push([ticker, exDividendDate]);
        }
    }

    return result;
}
describe('TestCheckDividendVariances', () => {
    it('should handle no inconsistencies', () => {
        const records = [
            ['AAPL', '2023-09-01', 0.22],
            ['AAPL', '2023-09-01', 0.22],
            ['MSFT', '2023-09-01', 0.56],
            ['GOOG', '2023-09-02', 0.00]
        ];
        const expectedOutput = [];
        expect(checkDividendVariances(records)).toEqual(expectedOutput);
    });

    it('should handle one inconsistency', () => {
        const records = [
            ['AAPL', '2023-09-01', 0.22],
            ['AAPL', '2023-09-01', 0.23],  // Different amount
            ['MSFT', '2023-09-01', 0.56],
            ['GOOG', '2023-09-02', 0.00]
        ];
        const expectedOutput = [['AAPL', '2023-09-01']];
        expect(checkDividendVariances(records)).toEqual(expectedOutput);
    });

    it('should handle multiple inconsistencies', () => {
        const records = [
            ['AAPL', '2023-09-01', 0.22],
            ['AAPL', '2023-09-01', 0.23],  // Different amount
            ['MSFT', '2023-09-01', 0.56],
            ['MSFT', '2023-09-01', 0.60],  // Different amount
            ['GOOG', '2023-09-02', 0.00],
            ['TSLA', '2023-09-03', 0.10],
            ['TSLA', '2023-09-03', 0.10],  // Same amount, no inconsistency
            ['TSLA', '2023-09-03', 0.15]  // Different amount
        ];
        const expectedOutput = [['AAPL', '2023-09-01'], ['MSFT', '2023-09-01'], ['TSLA', '2023-09-03']];
        expect(checkDividendVariances(records)).toEqual(expectedOutput);
    });

    it('should handle a single record', () => {
        const records = [
            ['AAPL', '2023-09-01', 0.22]
        ];
        const expectedOutput = [];
        expect(checkDividendVariances(records)).toEqual(expectedOutput);
    });

    it('should handle an empty list', () => {
        const records = [];
        const expectedOutput = [];
        expect(checkDividendVariances(records)).toEqual(expectedOutput);
    });
});
