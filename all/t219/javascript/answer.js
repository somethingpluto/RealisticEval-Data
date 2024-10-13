/**
 * Check for ticker symbols with the same ex-dividend date but different dividend amounts.
 *
 * Parameters:
 * - records (array of arrays): Each array contains [ticker, exDividendDate, dividendAmount].
 *
 * Returns:
 * - array of arrays: Each array contains [ticker, exDividendDate] that have different dividend amounts.
 */
function checkDividendVariances(records) {
    // Object to store dividend amounts by [ticker, exDividendDate]
    const dividendDict = {};

    // Iterate through the records
    for (const [ticker, exDividendDate, dividendAmount] of records) {
        const key = [ticker, exDividendDate].join('|'); // Use a string key for JavaScript objects
        if (!dividendDict[key]) {
            dividendDict[key] = new Set();
        }
        dividendDict[key].add(dividendAmount);
    }

    // Find entries with more than one unique dividend amount
    const result = Object.entries(dividendDict).filter(([key, amounts]) => amounts.size > 1).map(([key]) => {
        const [ticker, exDividendDate] = key.split('|');
        return [ticker, exDividendDate];
    });

    return result;
}