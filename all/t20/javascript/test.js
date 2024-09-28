const processMarkdown = require('./path/to/your/module'); // Adjust the path as necessary

describe('processMarkdown', () => {
    test('single asterisk pair', () => {
        const content = "This is a *test.js* string.";
        const expected = "This is a *test.js* string.";
        expect(processMarkdown(content)).toBe(expected);
    });

    test('nested asterisks', () => {
        const content = "Example of **nested *asterisks***.";
        const expected = "Example of *nested asterisks*.";
        expect(processMarkdown(content)).toBe(expected);
    });

    test('multiple asterisk pairs', () => {
        const content = "*Multiple* pairs of *asterisks* in *one* sentence.";
        const expected = "*Multiple pairs of asterisks in one* sentence.";
        expect(processMarkdown(content)).toBe(expected);
    });

    test('asterisks with no text', () => {
        const content = "Asterisks with ** no text.";
        const expected = "Asterisks with ** no text.";
        expect(processMarkdown(content)).toBe(expected);
    });

    test('asterisks around spaces', () => {
        const content = "Asterisks around * *spaces* * are tricky.";
        const expected = "Asterisks around * spaces * are tricky.";
        expect(processMarkdown(content)).toBe(expected);
    });
});