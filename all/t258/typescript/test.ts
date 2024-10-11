describe('extractCharacterBits', () => {
  it('should return the correct position and bits when character is found', () => {
    const byteArray = Buffer.from('Hello, World!', 'utf-8');
    const char = 'o';
    const result = extractCharacterBits(byteArray, char);

    expect(result).toEqual([4, '1100']);
  });

  it('should return null when character is not found', () => {
    const byteArray = Buffer.from('Hello, World!', 'utf-8');
    const char = 'z';
    const result = extractCharacterBits(byteArray, char);

    expect(result).toBeNull();
  });

  it('should handle different character encodings', () => {
    const byteArray = Buffer.from('你好，世界！', 'gbk'); // Assuming gbk encoding
    const char = '好';
    const result = extractCharacterBits(byteArray, char, 'gbk');

    expect(result).toEqual([0, '11100100']);
  });
});