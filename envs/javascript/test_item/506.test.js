/**
 * Convert a snake_case string to CamelCase.
 *
 * @param {string} snakeStr - The snake_case string to convert.
 * @returns {string} The converted CamelCase string.
 */
function snakeToCamel(snakeStr) {
    return snakeStr.replace(/([-_][a-z])/g, (group) =>
        group.toUpperCase().replace('-', '').replace('_', '')
    );
}
describe('Test snakeToCamel', () => {
    test('test basic snake_case to CamelCase conversion', () => {
        expect(snakeToCamel("hello_world")).toBe("HelloWorld");
    });

    test('test conversion of a snake_case string with multiple words', () => {
        expect(snakeToCamel("this_is_a_test")).toBe("ThisIsATest");
    });

    test('test conversion with numbers in the string', () => {
        expect(snakeToCamel("convert_this_123_string")).toBe("ConvertThis123String");
    });

    test('test conversion with leading and trailing underscores', () => {
        expect(snakeToCamel("_leading_and_trailing_")).toBe("LeadingAndTrailing");
        expect(snakeToCamel("___multiple___underscores___")).toBe("MultipleUnderscores");
    });

    test('test conversion of an empty string', () => {
        expect(snakeToCamel("")).toBe("");
    });
});
