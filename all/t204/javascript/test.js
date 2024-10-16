describe('splitString function', () => {
    test('Split a regular sentence', () => {
        const input = "Hello world from Catch2";
        const expected = ["Hello", "world", "from", "Catch2"];
        expect(splitString(input)).toEqual(expected);
    });

    test('Handle multiple spaces', () => {
        const input = "Multiple   spaces between words";
        const expected = ["Multiple", "spaces", "between", "words"];
        expect(splitString(input)).toEqual(expected);
    });

    test('Single word input', () => {
        const input = "Single";
        const expected = ["Single"];
        expect(splitString(input)).toEqual(expected);
    });

    test('Empty string input', () => {
        const input = "";
        const expected = [];
        expect(splitString(input)).toEqual(expected);
    });

    test('String with leading and trailing spaces', () => {
        const input = "   Leading and trailing spaces   ";
        const expected = ["Leading", "and", "trailing", "spaces"];
        expect(splitString(input)).toEqual(expected);
    });
});