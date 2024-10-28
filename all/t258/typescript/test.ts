describe('TestExtractCharacterBits', () => {
  it('test_case_1_valid_utf8', () => {
      const byteArray = new Uint8Array([72, 101, 108, 108, 111, 44, 32, 87, 111, 114, 108, 100, 33]);
      const char = 'W';
      const result = extractCharacterBits(byteArray, char, 'utf-8');
      const expectedResult = [7, '01010111'];  // 'W' is at position 7 with binary bits
      expect(result).toEqual(expectedResult);
  });

  it('test_case_2_non_existent_character', () => {
      const byteArray = new Uint8Array([84, 104, 105, 115, 32, 105, 115, 32, 97, 32, 116, 101, 115, 116, 46]);
      const char = 'z';
      const result = extractCharacterBits(byteArray, char, 'utf-8');
      expect(result).toBeNull();  // Character 'z' is not in the byte array
  });

  it('test_case_3_invalid_encoding', () => {
      const byteArray = new Uint8Array([255, 254]);
      const char = 'A';
      const result = extractCharacterBits(byteArray, char, 'ascii');  // Invalid bytes for ASCII
      expect(result).toBeNull();  // Should handle UnicodeDecodeError and return null
  });

  it('test_case_4_valid_utf16', () => {
      const byteString = 'Hello, World!';
      const byteArray = new Uint8Array(new TextEncoder().encode(byteString).buffer);
      const char = '!';
      const result = extractCharacterBits(byteArray, char, 'utf-16');
      const expectedResult = [12, '00100001 00000000'];  // '!' at position 12 in UTF-16 encoding
      expect(result).toEqual(expectedResult);
  });

  it('test_case_5_special_characters_utf8', () => {
      const byteString = 'Python 🐍 is fun!';
      const byteArray = new Uint8Array(new TextEncoder().encode(byteString).buffer);
      const char = '🐍';
      const result = extractCharacterBits(byteArray, char, 'utf-8');
      const expectedResult = [7, '11110000 10011111 10010000 10001101'];  // Unicode character 🐍 in UTF-8
      expect(result).toEqual(expectedResult);
  });
});