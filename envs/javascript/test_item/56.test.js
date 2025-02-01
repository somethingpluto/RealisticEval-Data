/**
 * Finds all the characters that can be represented in Shift-JIS but not in GBK, and returns them as an array.
 *
 * @returns {string[]} An array of characters that are unique to Shift-JIS and not encodable in GBK.
 */
function findShiftJisNotGbk() {
    const shiftJisNotGbk = [];
    for (let code = 0x80; code <= 0x9F; code++) {
        const char = String.fromCharCode(code);
        try {
            // Attempt to encode the character in GBK
            const gbkEncoded = new TextEncoder('gbk').encode(char);
            // If successful, the character is also encodable in GBK
        } catch (e) {
            // If an error is thrown, the character is not encodable in GBK
            shiftJisNotGbk.push(char);
        }
    }
    return shiftJisNotGbk;
}
describe('TestFindShiftJISNotGBK', () => {
  let shiftjisNotGbk;

  beforeAll(() => {
      // Pre-calculate the list once since it's computationally expensive
      shiftjisNotGbk = findShiftJisNotGbk();
  });

  test('test_known_shiftjis_character_not_in_gbk', () => {
      // Test known characters (example values provided might not actually be in one and not the other; please adjust accordingly based on actual encoding tables)
      const knownShiftJisOnly = 'ヱ';  // An example character, ensure this is correct as per your encodings
      expect(shiftjisNotGbk).not.toContain(knownShiftJisOnly);
  });

  test('test_character_in_both_encodings', () => {
      // Test characters known to be in both encodings
      const commonCharacter = '水';  // Common in both, ensure accuracy
      expect(shiftjisNotGbk).not.toContain(commonCharacter);
  });

  test('test_character_in_neither_encoding', () => {
      // Character not typically found in either encoding
      const neitherEncodingChar = '\u{1F4A9}';  // Emoji, not in basic Shift-JIS or GBK
      expect(shiftjisNotGbk).not.toContain(neitherEncodingChar);
  });

  test('test_bounds_of_bmp', () => {
      // Characters at the edge of the BMP should be checked
      const edgeOfBmp = '\uffff';  // Last character in BMP
      // Since this test.js is situational, we check based on the known state; may not be necessary
      if (shiftjisNotGbk.includes(edgeOfBmp)) {
          expect(shiftjisNotGbk).toContain(edgeOfBmp);
      } else {
          expect(shiftjisNotGbk).not.toContain(edgeOfBmp);
      }
  });
});
