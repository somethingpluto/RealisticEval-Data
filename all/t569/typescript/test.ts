describe('compressString', () => {
    it('should return the original string if it is shorter than the max length', () => {
        const input = "Short string";
        const result = compressString(input);
        expect(result).toBe(input);
    });

    it('should return the original string if it is exactly equal to the max length', () => {
        const input = "Exactly 18 chars";
        const result = compressString(input);
        expect(result).toBe(input);
    });

    it('should truncate the string and append "..." if it exceeds the max length', () => {
        const input = "This is a long string that needs to be compressed.";
        const result = compressString(input);
        expect(result).toBe("This is a long ...");
    });

    it('should truncate the string to maxLength - 3 and append "..." when maxLength is specified', () => {
        const input = "Another long string that is definitely too long.";
        const result = compressString(input, 25);
        expect(result).toBe("Another long string th...");
    });

    it('should use default max length of 18 if no maxLength is provided', () => {
        const input = "This string is way too long.";
        const result = compressString(input);
        expect(result).toBe("This string is ...");
    });

    it('should return the original string if it is empty', () => {
        const input = "";
        const result = compressString(input);
        expect(result).toBe(input);
    });
});