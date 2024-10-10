function checkDividendVariances(records) {
    /**
     * Check for ticker symbols with the same ex-dividend date but different dividend amounts.
     * @param {Array} records - Each array element contains [ticker, ex_dividend_date, dividend_amount].
     * @returns {Array} - Each array element contains [ticker, ex_dividend_date] that have different dividend amounts.
     */

    const varianceMap = {};
    const result = [];

    records.forEach(record => {
        const [ticker, exDividendDate, dividendAmount] = record;

        if (!varianceMap[ticker]) {
            varianceMap[ticker] = {};
        }

        if (!varianceMap[ticker][exDividendDate]) {
            varianceMap[ticker][exDividendDate] = [];
        }

        varianceMap[ticker][exDividendDate].push(dividendAmount);
    });

    Object.keys(varianceMap).forEach(ticker => {
        Object.keys(varianceMap[ticker]).forEach(exDividendDate => {
            if (varianceMap[ticker][exDividendDate].length > 1) {
                result.push([ticker, exDividendDate]);
            }
        });
    });

    return result;
}