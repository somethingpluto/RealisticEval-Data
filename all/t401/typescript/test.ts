describe('findPlaceholders', () => {
    it('should find placeholders correctly', () => {
        const text = 'This is a test with {{ placeholder1 }} and {{ placeholder2 }}.';
        const expected = ['{{ placeholder1 }}', '{{ placeholder2 }}'];
        expect(findPlaceholders(text)).toEqual(expected);
    });

    it('should handle empty string', () => {
        const text = '';
        const expected: string[] = [];
        expect(findPlaceholders(text)).toEqual(expected);
    });

    it('should handle string without placeholders', () => {
        const text = 'This is a plain text without any placeholders.';
        const expected: string[] = [];
        expect(findPlaceholders(text)).toEqual(expected);
    });

    it('should handle multiple consecutive placeholders', () => {
        const text = 'This is {{ one }} and {{ two }} and {{ three }}.';
        const expected = ['{{ one }}', '{{ two }}', '{{ three }}'];
        expect(findPlaceholders(text)).toEqual(expected);
    });
});