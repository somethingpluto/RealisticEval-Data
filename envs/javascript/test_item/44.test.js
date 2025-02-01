/**
 * Align two lines of string to the left, supplementing with spaces if the length is not enough.
 *
 * @param {string} str1 - The first string.
 * @param {string} str2 - The second string.
 * @returns {Array<string>} An array containing the aligned str1 and aligned str2.
 */
function alignLinesLeft(str1, str2) {
    const maxLength = Math.max(str1.length, str2.length);
    const alignedStr1 = str1.padEnd(maxLength, ' ');
    const alignedStr2 = str2.padEnd(maxLength, ' ');
    return [alignedStr1, alignedStr2];
}
describe('alignLinesLeft', () => {
  it('aligns equal length strings correctly', () => {
      const str1 = "Hello";
      const str2 = "World";
      const expected_str1 = "Hello";
      const expected_str2 = "World";
      const [aligned_str1, aligned_str2] = alignLinesLeft(str1, str2);
      expect(aligned_str1).toBe(expected_str1);
      expect(aligned_str2).toBe(expected_str2);
  });

  it('aligns first string longer than second', () => {
      const str1 = "Hello, World!";
      const str2 = "Hi";
      const expected_str1 = "Hello, World!";
      const expected_str2 = "Hi           ";  // 14 spaces after "Hi"
      const [aligned_str1, aligned_str2] = alignLinesLeft(str1, str2);
      expect(aligned_str1).toBe(expected_str1);
      expect(aligned_str2).toBe(expected_str2);
  });

  it('aligns second string longer than first', () => {
      const str1 = "Hey";
      const str2 = "Goodbye, friend!";
      const expected_str1 = "Hey             ";  // 15 spaces after "Hey"
      const expected_str2 = "Goodbye, friend!";
      const [aligned_str1, aligned_str2] = alignLinesLeft(str1, str2);
      expect(aligned_str1).toBe(expected_str1);
      expect(aligned_str2).toBe(expected_str2);
  });

  it('aligns empty first string', () => {
      const str1 = "";
      const str2 = "World";
      const expected_str1 = "     ";  // 5 spaces
      const expected_str2 = "World";
      const [aligned_str1, aligned_str2] = alignLinesLeft(str1, str2);
      expect(aligned_str1).toBe(expected_str1);
      expect(aligned_str2).toBe(expected_str2);
  });

  it('aligns empty second string', () => {
      const str1 = "Hello";
      const str2 = "";
      const expected_str1 = "Hello";
      const expected_str2 = "     ";  // 5 spaces
      const [aligned_str1, aligned_str2] = alignLinesLeft(str1, str2);
      expect(aligned_str1).toBe(expected_str1);
      expect(aligned_str2).toBe(expected_str2);
  });

  it('aligns both empty strings', () => {
      const str1 = "";
      const str2 = "";
      const expected_str1 = "";
      const expected_str2 = "";
      const [aligned_str1, aligned_str2] = alignLinesLeft(str1, str2);
      expect(aligned_str1).toBe(expected_str1);
      expect(aligned_str2).toBe(expected_str2);
  });

  it('aligns strings with spaces', () => {
      const str1 = "Hello ";
      const str2 = "World  ";
      const expected_str1 = "Hello  ";
      const expected_str2 = "World  ";
      const [aligned_str1, aligned_str2] = alignLinesLeft(str1, str2);
      expect(aligned_str1).toBe(expected_str1);
      expect(aligned_str2).toBe(expected_str2);
  });
});
