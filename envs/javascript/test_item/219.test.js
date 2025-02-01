/**
 * Check for ticker symbols with the same ex-dividend date but different dividend amounts.
 * @param {Array} records - An array of arrays, where each inner array contains [ticker, exDividendDate, dividendAmount].
 * @returns {Array} An array of arrays, where each inner array contains [ticker, exDividendDate] that have different dividend amounts.
 */
function checkDividendVariances(records) {
    const dateMap = new Map();

    records.forEach(record => {
        const [ticker, exDividendDate, dividendAmount] = record;
        const key = `${exDividendDate}`;

        if (!dateMap.has(key)) {
            dateMap.set(key, new Map());
        }

        const tickerMap = dateMap.get(key);
        if (tickerMap.has(ticker)) {
            const existingAmount = tickerMap.get(ticker);
            if (existingAmount !== dividendAmount) {
                tickerMap.set(ticker, dividendAmount);
            }
        } else {
            tickerMap.set(ticker, dividendAmount);
        }
    });

    const result = [];
    dateMap.forEach((tickerMap, exDividendDate) => {
        if (tickerMap.size > 1) {
            const tickers = Array.from(tickerMap.keys());
            result.push([tickers.join(','), exDividendDate]);
        }
    });

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
