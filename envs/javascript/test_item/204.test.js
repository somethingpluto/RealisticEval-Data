/**
 * Split a string into multiple substrings based on spaces and return an array containing these substrings.
 *
 * @param {string} str The input string to be split into words.
 * @return {string[]} An array of strings, each representing a word from the input string. Returns an empty array if the input string is empty or contains only spaces.
 */
function splitString(str) {
    // Trim the input string to remove leading and trailing spaces
    const trimmedStr = str.trim();

    // Check if the trimmed string is empty
    if (trimmedStr === '') {
        return [];
    }

    // Split the string by spaces and return the resulting array
    return trimmedStr.split(/\s+/);
}
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
