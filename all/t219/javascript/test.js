describe('checkDividendVariances', () => {
    it('should return tickers with the same ex-dividend date but different dividend amounts', () => {
        const records = [
            ['AAPL', '2023-04-14', 50],
            ['AAPL', '2023-04-14', 60], // Different dividend amount
            ['GOOGL', '2023-04-15', 2800],
            ['GOOGL', '2023-04-15', 2800], // Same dividend amount
            ['MSFT', '2023-04-16', 310]
        ];

        const expected = [
            ['AAPL', '2023-04-14']
        ];

        expect(checkDividendVariances(records)).toEqual(expected);
    });

    it('should handle empty input gracefully', () => {
        const records = [];
        const expected = [];
        expect(checkDividendVariances(records)).toEqual(expected);
    });

    it('should handle single record correctly', () => {
        const records = [['AAPL', '2023-04-14', 50]];
        const expected = [];
        expect(checkDividendVariances(records)).toEqual(expected);
    });
});