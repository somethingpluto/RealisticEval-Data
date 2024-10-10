describe('extractCharacterBits', () => {
    test('should return position and bits for existing char', () => {
        const byteArray = Buffer.from([0x41, 0x62, 0x63]);  // 'abc'
        const char = 'b';
        const expectedResult = [1, '01100010'];
        const result = extractCharacterBits(byteArray, char);
        expect(result).toEqual(expectedResult);
    });

    test('should return null for nonexistent char', () => {
        const byteArray = Buffer.from([0x41, 0x62, 0x63]);  // 'abc'
        const char = 'd';
        const expectedResult = null;
        const result = extractCharacterBits(byteArray, char);
        expect(result).toBeNull();
    });
});