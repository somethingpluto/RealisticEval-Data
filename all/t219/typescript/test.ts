describe('checkDividendVariances', () => {
    it('should return tickers with the same ex-dividend date but different dividend amounts', () => {
      const records = [
        ['AAPL', '2023-10-05', 0.75],
        ['GOOGL', '2023-10-05', 0.65],
        ['AAPL', '2023-10-05', 0.85], // Different amount for AAPL
        ['MSFT', '2023-10-05', 0.45],
        ['MSFT', '2023-10-05', 0.45] // Same amount for MSFT
      ];
  
      const expected = [
        ['AAPL', '2023-10-05']
      ];
  
      expect(checkDividendVariances(records)).toEqual(expected);
    });
  });