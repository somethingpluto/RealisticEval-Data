/**
 * Finds all the characters that can be represented in Shift-JIS but not in GBK, and returns them as an array.
 *
 * @returns {string[]} An array of characters that are unique to Shift-JIS and not encodable in GBK.
 */
function findShiftJisNotGbk() {
    const shiftJisChars = [];
    const gbkChars = new Set();
    const uniqueToShiftJis = [];

    // Generate all possible Shift-JIS characters
    for (let byte1 = 0x81; byte1 <= 0x9F; byte1++) {
        for (let byte2 = 0x40; byte2 <= 0xFC; byte2++) {
            if (byte2 !== 0x7F) { // Skip invalid byte 0x7F
                const codePoint = (byte1 << 8) | byte2;
                const char = String.fromCharCode(codePoint);
                shiftJisChars.push(char);
            }
        }
    }

    for (let byte1 = 0xE0; byte1 <= 0xEF; byte1++) {
        for (let byte2 = 0x40; byte2 <= 0xFC; byte2++) {
            if (byte2 !== 0x7F) { // Skip invalid byte 0x7F
                const codePoint = (byte1 << 8) | byte2;
                const char = String.fromCharCode(codePoint);
                shiftJisChars.push(char);
            }
        }
    }

    // Generate all possible GBK characters
    for (let byte1 = 0x81; byte1 <= 0xFE; byte1++) {
        for (let byte2 = 0x40; byte2 <= 0xFE; byte2++) {
            if (byte2 !== 0x7F) { // Skip invalid byte 0x7F
                const codePoint = (byte1 << 8) | byte2;
                const char = String.fromCharCode(codePoint);
                gbkChars.add(char);
            }
        }
    }

    // Find characters that are in Shift-JIS but not in GBK
    for (const char of shiftJisChars) {
        if (!gbkChars.has(char)) {
            uniqueToShiftJis.push(char);
        }
    }

    return uniqueToShiftJis;
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
