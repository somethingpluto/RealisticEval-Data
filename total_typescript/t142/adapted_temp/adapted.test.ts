describe('convertCamelCaseToSentence', () => {
    test('should convert a simple camelCase string to a sentence', () => {
        const input = "thisIsTest";
        const expectedOutput = "This Is Test";
        expect(camelCaseToCapitalizedWithSpaces(input)).toBe(expectedOutput);
    });

    test('should handle single word starting with lowercase', () => {
        const input = "example";
        const expectedOutput = "Example";
        expect(camelCaseToCapitalizedWithSpaces(input)).toBe(expectedOutput);
    });

    test('should handle a camelCase string with multiple uppercase letters', () => {
        const input = "thisIsAnExampleString";
        const expectedOutput = "This Is An Example String";
        expect(camelCaseToCapitalizedWithSpaces(input)).toBe(expectedOutput);
    });

    test('should handle a single uppercase letter', () => {
        const input = "aSingleUppercaseLetterX";
        const expectedOutput = "A Single Uppercase Letter X";
        expect(camelCaseToCapitalizedWithSpaces(input)).toBe(expectedOutput);
    });

    test('should handle an already capitalized string', () => {
        const input = "AlreadyCapitalized";
        const expectedOutput = "Already Capitalized";
        expect(camelCaseToCapitalizedWithSpaces(input)).toBe(expectedOutput);
    });
});
function camelCaseToCapitalizedWithSpaces(input: string): string {
    // Use a regular expression to insert spaces before capital letters and numbers
    const spacedString = input.replace(/([A-Z0-9])/g, ' $1');

    // Capitalize the first letter of each word
    const capitalizedString = spacedString
        .split(' ')
        .map(word => word.charAt(0).toUpperCase() + word.slice(1))
        .join(' ');

    // Trim any leading spaces and return the result
    return capitalizedString.trim();
}