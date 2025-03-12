/**
 * Compresses an HTML string by removing unnecessary whitespace without disrupting
 * the integrity of content within <pre>, <div>, <script>, and <style> tags.
 *
 * @param {string} htmlString - The HTML content to compress.
 * @returns {string} The compressed HTML content.
 */
function compressHTML(htmlString) {
    // Regular expression to match HTML tags and content within <pre>, <div>, <script>, and <style> tags
    const regex = /(<pre[^>]*>.*?<\/pre>|<div[^>]*>.*?<\/div>|<script[^>]*>.*?<\/script>|<style[^>]*>.*?<\/style>|<[^>]+>|[^<>\s]+)/gs;

    // Split the HTML string into parts based on the regex
    const parts = htmlString.match(regex);

    // Initialize an array to hold the compressed parts
    const compressedParts = [];

    // Iterate over each part
    parts.forEach(part => {
        if (part.startsWith('<pre') || part.startsWith('<div') || part.startsWith('<script') || part.startsWith('<style')) {
            // If the part is a <pre>, <div>, <script>, or <style> tag, keep it as is
            compressedParts.push(part);
        } else if (part.startsWith('<') && part.endsWith('>')) {
            // If the part is a regular HTML tag, trim its whitespace
            compressedParts.push(part.trim());
        } else {
            // If the part is plain text, compress its whitespace
            compressedParts.push(part.replace(/\s+/g, ' ').trim());
        }
    });

    // Join the compressed parts back into a single string
    return compressedParts.join('');
}
describe('compressHTML', () => {
    test('should remove leading and trailing spaces around tags', () => {
        const input = '  <div>  <p>Test</p>  </div>  ';
        const expected = '<div><p>Test</p></div>';
        expect(compressHTML(input)).toBe(expected);
    });

    test('should replace multiple newlines with a single space', () => {
        const input = '<div>\n\n<p>Test</p>\n\n</div>';
        const expected = '<div> <p>Test</p> </div>';
        expect(compressHTML(input)).toBe(expected);
    });

    test('should remove unnecessary spaces within text', () => {
        const input = '<p>This    is a test</p>';
        const expected = '<p>This is a test</p>';
        expect(compressHTML(input)).toBe(expected);
    });

    test('should handle empty strings', () => {
        const input = '';
        const expected = '';
        expect(compressHTML(input)).toBe(expected);
    });

    test('should process complex nested HTML correctly', () => {
        const input = '<div>   <span>    Text <i>    Italic </i> more text </span>   </div>';
        const expected = '<div><span>Text <i>Italic</i> more text</span></div>';
        expect(compressHTML(input)).toBe(expected);
    });

    test('should not disrupt content within <pre> and <textarea> tags', () => {
        const input = '<pre>\n    function example() {\n        console.log("example");\n    }\n</pre>';
        const expected = '<pre>\n    function example() {\n        console.log("example");\n    }\n</pre>'; // assuming no changes in <pre> and <textarea>
        expect(compressHTML(input)).toBe(expected);
    });

    test('should handle HTML with attributes correctly', () => {
        const input = '<a href="http://example.com"    title="Example" >Link</a>';
        const expected = '<a href="http://example.com" title="Example">Link</a>';
        expect(compressHTML(input)).toBe(expected);
    });
});
