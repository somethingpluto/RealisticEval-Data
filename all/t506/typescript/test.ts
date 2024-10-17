describe('Test snakeToCamel', () => {
    it('test basic conversion', () => {
        // Test basic snake_case to CamelCase conversion
        expect(snakeToCamel("hello_world")).toBe("HelloWorld");
    });

    it('test conversion of a snake_case string with multiple words', () => {
        // Test conversion of a snake_case string with multiple words
        expect(snakeToCamel("this_is_a_test")).toBe("ThisIsATest");
    });

    it('test conversion with numbers in the string', () => {
        // Test conversion with numbers in the string
        expect(snakeToCamel("convert_this_123_string")).toBe("ConvertThis123String");
    });

    it('test conversion with leading and trailing underscores', () => {
        // Test conversion with leading and trailing underscores
        expect(snakeToCamel("_leading_and_trailing_")).toBe("LeadingAndTrailing");
        expect(snakeToCamel("___multiple___underscores___")).toBe("MultipleUnderscores");
    });

    it('test conversion of an empty string', () => {
        // Test conversion of an empty string
        expect(snakeToCamel("")).toBe("");
    });
});