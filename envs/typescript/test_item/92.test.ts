import { JSDOM } from 'jsdom';

const dom = new JSDOM();
const { document } = dom.window;

function replaceHtmlEntities(htmlString: string): string {
    // Function implementation goes here
}
describe('replaceHtmlEntities', () => {
    test('decodes standard HTML entities', () => {
        const input: string = 'The &amp; symbol should become an &quot;and&quot; sign.';
        const expected: string = 'The & symbol should become an "and" sign.';
        expect(replaceHtmlEntities(input)).toBe(expected);
    });

    test('returns empty string for empty input', () => {
        const input: string = '';
        const expected: string = '';
        expect(replaceHtmlEntities(input)).toBe(expected);
    });

    test('decodes multiple different entities in one string', () => {
        const input: string = '&lt;div&gt;Hello &amp; Welcome to the &apos;World&apos;!&lt;/div&gt;';
        const expected: string = '<div>Hello & Welcome to the \'World\'!</div>';
        expect(replaceHtmlEntities(input)).toBe(expected);
    });

    test('handles strings with no entities', () => {
        const input: string = 'Just a normal string without entities.';
        const expected: string = 'Just a normal string without entities.';
        expect(replaceHtmlEntities(input)).toBe(expected);
    });
});
