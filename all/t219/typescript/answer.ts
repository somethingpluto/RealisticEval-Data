function checkDividendVariances(records: [string, string, number][]): [string, string][] {
    // Dictionary to store dividend amounts by (ticker, exDividendDate)
    const dividendDict: Map<[string, string], Set<number>> = new Map();

    // Iterate through the records
    for (const [ticker, exDividendDate, dividendAmount] of records) {
        const key: [string, string] = [ticker, exDividendDate];
        if (!dividendDict.has(key)) {
            dividendDict.set(key, new Set());
        }
        dividendDict.get(key)?.add(dividendAmount);
    }

    // Find entries with more than one unique dividend amount
    const result: [string, string][] = [];
    for (const [key, amounts] of dividendDict) {
        if (amounts.size > 1) {
            result.push([key[0], key[1]]);
        }
    }

    return result;
}