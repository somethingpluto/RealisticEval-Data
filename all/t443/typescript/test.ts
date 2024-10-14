// compress-whitespace.ts
function compressWhitespace(inputString: string): string {
    return inputString.replace(/\s+/g, ' ').trim();
}

export default compressWhitespace;

// compress-whitespace.test.ts
import compressWhitespace from './compress-whitespace';

describe('compressWhitespace', () => {
    it('should compress multiple consecutive whitespace characters into a single space', () => {
        expect(compressWhitespace('foo')).toBe('foo');
        expect(compressWhitespace(' foo')).toBe('foo');
        expect(compressWhitespace('foo ')).toBe('foo');
        expect(compressWhitespace('  foo  ')).toBe('foo');
        expect(compressWhitespace('foo  bar')).toBe('foo bar');
        expect(compressWhitespace('  foo  bar  ')).toBe('foo bar');
    });
});

// package.json
{
  "scripts": {
    "test": "jest"
  }
}

// Assuming you have jest and ts-jest setup