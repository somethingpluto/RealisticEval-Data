// Import the replaceHtmlEntities function if it's in another file
// const replaceHtmlEntities = require('./path_to_your_file');
// Mock DOMParser in global scope
global.DOMParser = class {
  parseFromString(str) {
    return {
      documentElement: {
        textContent: str.replace(/&amp;/g, '&')
                        .replace(/&lt;/g, '<')
                        .replace(/&gt;/g, '>')
                        .replace(/&quot;/g, '"')
                        .replace(/&apos;/g, '\'')
      }
    };
  }
};
describe('replaceHtmlEntities', () => {
    test('decodes standard HTML entities', () => {
        const input = 'The &amp; symbol should become an &quot;and&quot; sign.';
        const expected = 'The & symbol should become an "and" sign.';
        expect(replaceHtmlEntities(input)).toBe(expected);
    });

    test('returns empty string for empty input', () => {
        const input = '';
        const expected = '';
        expect(replaceHtmlEntities(input)).toBe(expected);
    });

    test('throws TypeError when input is not a string', () => {
        const input = 123;
        expect(() => replaceHtmlEntities(input)).toThrow(TypeError);
    });

    test('decodes multiple different entities in one string', () => {
        const input = '&lt;div&gt;Hello &amp; Welcome to the &apos;World&apos;!&lt;/div&gt;';
        const expected = '<div>Hello & Welcome to the \'World\'!</div>';
        expect(replaceHtmlEntities(input)).toBe(expected);
    });

    test('handles strings with no entities', () => {
        const input = 'Just a normal string without entities.';
        const expected = 'Just a normal string without entities.';
        expect(replaceHtmlEntities(input)).toBe(expected);
    });
});