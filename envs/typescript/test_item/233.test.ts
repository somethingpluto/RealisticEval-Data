import { stripIndent } from 'common-tags';

/**
 * Removes comments from the provided string. Comments start with a '#' and end at the newline.
 * 
 * Example:
 *   Input: "Hello, world! # This is a comment"
 *   Output: "Hello, world!"
 * 
 * @param {string} input - The input string containing potential comments.
 * @returns {string} - The string with all comments removed.
 */
function removeComments(input: string): string {
  return input.split('\n').map(line => line.split('#')[0].trim()).join('\n');
}
describe('TestRemoveComments', () => {
    it('should handle a single line comment', () => {
      const inputString = "Hello, world!# This is a comment";
      const expectedOutput = "Hello, world!";
      expect(removeComments(inputString)).toEqual(expectedOutput);
    });
  
    it('should handle a string with no comments', () => {
      const inputString = "Hello, world!\nPython is fun!";
      const expectedOutput = "Hello, world!\nPython is fun!";
      expect(removeComments(inputString)).toEqual(expectedOutput);
    });
  
    it('should handle an empty string', () => {
      const inputString = "";
      const expectedOutput = "";
      expect(removeComments(inputString)).toEqual(expectedOutput);
    });
  
    it('should handle a string where all lines are comments', () => {
      const inputString = "# comment only line\n#another comment line";
      const expectedOutput = "\n";
      expect(removeComments(inputString)).toEqual(expectedOutput);
    });
  });
