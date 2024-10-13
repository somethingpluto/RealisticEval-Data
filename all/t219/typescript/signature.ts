/**
 * Check for ticker symbols with the same ex-dividend date but different dividend amounts.
 * 
 * @param records - An array of tuples, where each tuple contains (ticker, exDividendDate, dividendAmount).
 * @returns An array of tuples, where each tuple contains (ticker, exDividendDate) that have different dividend amounts.
 */
function checkDividendVariances(records: [string, string, number][]): [string, string][] {}