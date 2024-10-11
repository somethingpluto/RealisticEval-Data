interface Record {
    ticker: string;
    exDividendDate: string;
    dividendAmount: number;
}

function checkDividendVariances(records: Record[]): Record[] {
    const result: Record[] = [];
    const map = new Map<string, { dates: Set<string>, amounts: Set<number> }>();

    for (const record of records) {
        const key = `${record.ticker}-${record.exDividendDate}`;
        if (!map.has(key)) {
            map.set(key, { dates: new Set(), amounts: new Set() });
        }
        map.get(key).dates.add(record.exDividendDate);
        map.get(key).amounts.add(record.dividendAmount);
    }

    for (const [key, value] of map.entries()) {
        if (value.dates.size === 1 && value.amounts.size > 1) {
            const [ticker, exDividendDate] = key.split('-');
            result.push({ ticker, exDividendDate, dividendAmount: NaN }); // Assuming dividend amount is not relevant here
        }
    }

    return result;
}