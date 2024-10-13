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