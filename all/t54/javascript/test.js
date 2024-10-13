describe('TestRemoveTripleBackticks', () => {
  describe('Basic functionality', () => {
      it('should handle basic removal of triple backticks', () => {
          const inputStrings = ['Here is ```code``` example', 'Another ```example``` here', 'No backticks here'];
          const expectedOutput = ['Here is code example', 'Another example here', 'No backticks here'];
          expect(removeTripleBackticks(inputStrings)).toEqual(expectedOutput);
      });
  });

  describe('Strings with multiple instances of triple backticks', () => {
      it('should handle multiple instances of triple backticks', () => {
          const inputStrings = ['Multiple ```backticks``` in ```one``` string'];
          const expectedOutput = ['Multiple backticks in one string'];
          expect(removeTripleBackticks(inputStrings)).toEqual(expectedOutput);
      });
  });

  describe('Empty strings', () => {
      it('should handle empty strings', () => {
          const inputStrings = [''];
          const expectedOutput = [''];
          expect(removeTripleBackticks(inputStrings)).toEqual(expectedOutput);
      });
  });

  describe('Strings without triple backticks', () => {
      it('should handle strings without triple backticks', () => {
          const inputStrings = ['Just a normal string', 'Another normal string'];
          const expectedOutput = ['Just a normal string', 'Another normal string'];
          expect(removeTripleBackticks(inputStrings)).toEqual(expectedOutput);
      });
  });

  describe('Edge cases', () => {
      it('should handle edge cases like strings made entirely of triple backticks', () => {
          const inputStrings = ['```', '```more```', 'text``````'];
          const expectedOutput = ['', 'more', 'text'];
          expect(removeTripleBackticks(inputStrings)).toEqual(expectedOutput);
      });
  });
});