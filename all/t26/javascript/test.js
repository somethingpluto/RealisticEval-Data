describe('TestConvertToCommaSeparated', () => {
    it('should convert basic separators correctly', () => {
        expect(convertToCommaSeparated("apple;banana*orange/mango")).toBe("apple,banana,orange,mango");
    });

    it('should convert mixed separators in a string correctly', () => {
        expect(convertToCommaSeparated("grapes;lemon/melon*kiwi;litchi")).toBe("grapes,lemon,melon,kiwi,litchi");
    });

    it('should convert mixed separators in a string correctly (second test)', () => {
        expect(convertToCommaSeparated("grapes/lemon/melon*kiwi*litchi")).toBe("grapes,lemon,melon,kiwi,litchi");
    });

    it('should handle strings with no separators correctly', () => {
        expect(convertToCommaSeparated("watermelon")).toBe("watermelon");
    });
});