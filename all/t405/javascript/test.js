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