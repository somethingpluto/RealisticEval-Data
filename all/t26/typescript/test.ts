describe('convertToCommaSeparated', () => {
    it('should convert basic separators', () => {
        expect(convertToCommaSeparated("apple;banana*orange/mango")).toBe("apple,banana,orange,mango");
    });

    it('should convert mixed separators in a string', () => {
        expect(convertToCommaSeparated("grapes;lemon/melon*kiwi;litchi")).toBe("grapes,lemon,melon,kiwi,litchi");
    });

    it('should convert mixed separators in another string', () => {
        expect(convertToCommaSeparated("grapes/lemon/melon*kiwi*litchi")).toBe("grapes,lemon,melon,kiwi,litchi");
    });

    it('should handle strings without separators', () => {
        expect(convertToCommaSeparated("watermelon")).toBe("watermelon");
    });
});