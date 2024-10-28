describe('remove_inner_asterisks', () => {
    test('basic case', () => {
        const text = "Hello (*wo*rld*)!";
        const expected = "Hello (*world*)!";
        expect(removeInnerAsterisks(text)).toBe(expected);
    });

    test('multiple asterisks', () => {
        const text = "(*he*l*lo*)";
        const expected = "(*hello*)";
        expect(removeInnerAsterisks(text)).toBe(expected);
    });

    test('no asterisks inside', () => {
        const text = "(*hello*)";
        const expected = "(*hello*)";
        expect(removeInnerAsterisks(text)).toBe(expected);
    });

    test('multiple patterns', () => {
        const text = "(*hi*), (*there*), (*world*)!";
        const expected = "(*hi*), (*there*), (*world*)!";
        expect(removeInnerAsterisks(text)).toBe(expected);
    });

    test('no matching pattern', () => {
        const text = "This is a test without matching parentheses.";
        const expected = "This is a test without matching parentheses.";
        expect(removeInnerAsterisks(text)).toBe(expected);
    });
});