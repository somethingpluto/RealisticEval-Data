/**
 * Extracts the position and bits of a specific character from a byte array.
 *
 * @param {Uint8Array} byteArray - The byte array to search within.
 * @param {string} char - The character to find in the byte array.
 * @param {string} [charset='utf-8'] - The character encoding of the byte array.
 * @returns {Array|undefined} - A tuple of (position, bits) if the character is found, otherwise undefined.
 */
function extractCharacterBits(byteArray, char, charset = 'utf-8') {
  const encoder = new TextEncoder(charset);
  const decoder = new TextDecoder(charset);
  const charBytes = encoder.encode(char);
  const charBits = charBytes.map(byte => byte.toString(2).padStart(8, '0')).join('');

  for (let i = 0; i < byteArray.length; i++) {
    const byte = byteArray[i];
    const byteBits = byte.toString(2).padStart(8, '0');
    if (byteBits === charBits) {
      return [i, byteBits];
    }
  }

  return undefined;
}
describe('TestExtractCharacterBits', () => {
    it('test_case_1_valid_utf8', () => {
        const byte_array = new Uint8Array([72, 101, 108, 108, 111, 44, 32, 87, 111, 114, 108, 100, 33]);
        const char = 'W';
        const result = extractCharacterBits(byte_array, char, 'utf-8');
        const expected_result = [7, '01010111'];  // 'W' is at position 7 with binary bits
        expect(result).toEqual(expected_result);
    });

    it('test_case_2_non_existent_character', () => {
        const byte_array = new Uint8Array([84, 104, 105, 115, 32, 105, 115, 32, 97, 32, 116, 101, 115, 116, 46]);
        const char = 'z';
        const result = extractCharacterBits(byte_array, char, 'utf-8');
        expect(result).toBeUndefined();  // Character 'z' is not in the byte array
    });

    it('test_case_3_invalid_encoding', () => {
        const byte_array = new Uint8Array([255, 254]);
        const char = 'A';
        const result = extractCharacterBits(byte_array, char, 'ascii');  // Invalid bytes for ASCII
        expect(result).toBeUndefined();  // Should handle UnicodeDecodeError and return undefined
    });

    it('test_case_4_valid_utf16', () => {
        const byte_array = new Uint8Array([0, 72, 0, 101, 0, 108, 0, 108, 0, 111, 0, 44, 0, 32, 0, 87, 0, 111, 0, 114, 0, 108, 0, 100, 0, 33, 0, 0]);
        const char = '!';
        const result = extractCharacterBits(byte_array, char, 'utf-16');
        const expected_result = [12, '00100001 00000000'];  // '!' at position 12 in UTF-16 encoding
        expect(result).toEqual(expected_result);
    });

    it('test_case_5_special_characters_utf8', () => {
        const byte_array = new Uint8Array([80, 121, 116, 104, 111, 110, 240, 149, 145, 133, 105, 115, 32, 102, 117, 110, 33]);
        const char = '🐍';
        const result = extractCharacterBits(byte_array, char, 'utf-8');
        const expected_result = [7, '11110000 10011111 10010000 10001101'];  // Unicode character 🐍 in UTF-8
        expect(result).toEqual(expected_result);
    });
});
