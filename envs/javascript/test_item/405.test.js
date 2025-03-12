/**
 * Remove the part before the first uppercase letter and the first lowercase letter from the string.
 *
 * @param {...string} strings - Accepts one or more strings as variable arguments
 * @returns {Array<string>} - An array of processed strings
 */
function removePartsOfString(...strings) {
    return strings.map(str => {
        const upperCaseIndex = str.search(/[A-Z]/);
        const lowerCaseIndex = str.search(/[a-z]/);

        if (upperCaseIndex === -1 || lowerCaseIndex === -1) {
            return str; // If no uppercase or lowercase letter is found, return the original string
        }

        const firstIndex = Math.min(upperCaseIndex, lowerCaseIndex);
        return str.slice(firstIndex);
    });
}
describe('TestRemovePartsOfString', () => {
  it('should handle a string with no uppercase letters', () => {
      const result = removePartsOfString("abcdefg");
      expect(result).toEqual(["abcdefg"]);
  });

  it('should handle a string with no lowercase letters', () => {
      const result = removePartsOfString("ABCDEFG");
      expect(result).toEqual(["ABCDEFG"]);
  });

  it('should handle a string with mixed cases', () => {
      const result = removePartsOfString("1234AbCde5678");
      expect(result).toEqual(["AbCde5678"]);
  });

  it('should handle an empty string', () => {
      const result = removePartsOfString("");
      expect(result).toEqual([""]);
  });

  it('should handle a string with only one uppercase letter', () => {
      const result = removePartsOfString("X");
      expect(result).toEqual(["X"]);
  });

  it('should handle a string with only one lowercase letter', () => {
      const result = removePartsOfString("y");
      expect(result).toEqual(["y"]);
  });
});
