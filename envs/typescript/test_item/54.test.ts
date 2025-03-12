import { sanitizeString } from './stringSanitizer';

/**
 * Processes a list of strings, removing all occurrences of three consecutive backticks from each string.
 * 
 * @param stringList - The list of strings to process.
 * @returns A new list with all instances of three consecutive backticks removed from each string.
 */
function removeTripleBackticks(stringList: string[]): string[] {
    return stringList.map(sanitizeString);
}
describe('TestRemoveTripleBackticks', () => {
    it('test_remove_triple_backticks_basic', () => {
      // Test basic functionality
      const inputStrings = ['Here is ```code``` example', 'Another ```example``` here', 'No backticks here'];
      const expectedOutput = ['Here is code example', 'Another example here', 'No backticks here'];
      expect(removeTripleBackticks(inputStrings)).toEqual(expectedOutput);
    });
  
    it('test_strings_with_multiple_instances', () => {
      // Test strings containing multiple instances of triple backticks
      const inputStrings = ['Multiple ```backticks``` in ```one``` string'];
      const expectedOutput = ['Multiple backticks in one string'];
      expect(removeTripleBackticks(inputStrings)).toEqual(expectedOutput);
    });
  
    it('test_empty_strings', () => {
      // Test with empty strings
      const inputStrings = [''];
      const expectedOutput = [''];
      expect(removeTripleBackticks(inputStrings)).toEqual(expectedOutput);
    });
  
    it('test_no_triple_backticks', () => {
      // Test strings that do not contain triple backticks
      const inputStrings = ['Just a normal string', 'Another normal string'];
      const expectedOutput = ['Just a normal string', 'Another normal string'];
      expect(removeTripleBackticks(inputStrings)).toEqual(expectedOutput);
    });
  
    it('test_edge_cases', () => {
      // Test edge cases like strings made entirely of triple backticks
      const inputStrings = ['```', '```more```', 'text``````'];
      const expectedOutput = ['', 'more', 'text'];
      expect(removeTripleBackticks(inputStrings)).toEqual(expectedOutput);
    });
  });
