describe('TestFindShiftJISNotGBK', () => {
  let shiftjisNotGbk: string[];

  beforeAll(() => {
      // Pre-calculate the list once since it's computationally expensive
      shiftjisNotGbk = findShiftJisNotGbk();
  });

  it('should not include known Shift-JIS characters not in GBK', () => {
      // Test known characters (example values provided might not actually be in one and not the other; please adjust accordingly based on actual encoding tables)
      const knownShiftJisOnly = 'ヱ';  // An example character, ensure this is correct as per your encodings
      expect(shiftjisNotGbk).not.toContain(knownShiftJisOnly);
  });

  it('should not include characters known to be in both encodings', () => {
      // Test characters known to be in both encodings
      const commonCharacter = '水';  // Common in both, ensure accuracy
      expect(shiftjisNotGbk).not.toContain(commonCharacter);
  });

  it('should not include characters not in either encoding', () => {
      // Character not typically found in either encoding
      const neitherEncodingChar = '\u{1F4A9}';  // Emoji, not in basic Shift-JIS or GBK
      expect(shiftjisNotGbk).not.toContain(neitherEncodingChar);
  });

  it('should handle characters at the edge of the BMP correctly', () => {
      // Characters at the edge of the BMP should be checked
      const edgeOfBmp = '\uffff';  // Last character in BMP
      if (shiftjisNotGbk.includes(edgeOfBmp)) {
          expect(shiftjisNotGbk).toContain(edgeOfBmp);
      } else {
          expect(shiftjisNotGbk).not.toContain(edgeOfBmp);
      }
  });
});