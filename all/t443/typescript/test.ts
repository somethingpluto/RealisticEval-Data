describe('compressWhitespace', () => {
    it('should handle strings with single spaces', () => {
        expect(compressWhitespace("This is a test string.")).toBe("This is a test string.");
    });

    it('should handle strings with multiple spaces', () => {
        expect(compressWhitespace("This    is  a   test   string.")).toBe("This is a test string.");
    });

    it('should handle strings with leading and trailing spaces', () => {
        expect(compressWhitespace("   Leading and trailing spaces   ")).toBe("Leading and trailing spaces");
    });

    it('should handle strings with only spaces', () => {
        expect(compressWhitespace("       ")).toBe("");
    });

    it('should handle empty strings', () => {
        expect(compressWhitespace("")).toBe("");
    });
});