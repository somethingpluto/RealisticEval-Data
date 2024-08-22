describe('getCSSFromSheet', () => {
    let mockSheet;

    beforeEach(() => {
        // Create a mock CSSStyleSheet object with cssRules
        mockSheet = {
            cssRules: [
                { cssText: 'body { background-color: red; }' },
                { cssText: 'p { color: blue; }' }
            ]
        };
    });

    test('correctly concatenates cssText from all rules', () => {
        const expected = 'body { background-color: red; }p { color: blue; }';
        expect(getCSSFromSheet(mockSheet)).toBe(expected);
    });

    test('returns empty string for sheets with no cssRules', () => {
        const emptySheet = { cssRules: [] };
        expect(getCSSFromSheet(emptySheet)).toBe('');
    });

    test('handles sheets where cssRules is undefined', () => {
        const undefinedRulesSheet = {};
        expect(getCSSFromSheet(undefinedRulesSheet)).toBe('');
    });

    test('throws TypeError if input is not a CSSStyleSheet', () => {
        const invalidInput = 'Not a StyleSheet';
        expect(() => getCSSFromSheet(invalidInput)).toThrow(TypeError);
    });

    test('handles exceptions from accessing cssRules (e.g., CORS issues)', () => {
        // Simulate a CORS issue where accessing cssRules throws an error
        const inaccessibleSheet = {
            get cssRules() {
                throw new Error('Security error: Access is denied.');
            }
        };
        expect(getCSSFromSheet(inaccessibleSheet)).toBe('');
    });
});