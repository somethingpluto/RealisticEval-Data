/**
 * Compresses an HTML string by removing unnecessary whitespace,
 * including newlines, tabs, and extra spaces,
 * while preserving the structure of the HTML.
 *
 * @param {string} html - The input HTML string to be compressed.
 * @returns {string} - The compressed HTML string with reduced whitespace.
 */
function compressHtml(html) {
    // Remove comments
    html = html.replace(/<!--[\s\S]*?-->/g, '');

    // Remove newlines, tabs, and multiple spaces
    html = html.replace(/\s+/g, ' ');

    // Remove spaces around tags
    html = html.replace(/>\s+</g, '><');

    // Trim leading and trailing spaces
    html = html.trim();

    return html;
}
describe('compressHtml', () => {
    it('should remove newlines and tabs', () => {
        const input = `
            <div>
                <p>Test paragraph.</p>
            </div>
        `;
        const expectedOutput = '<div><p>Test paragraph.</p></div>';
        expect(compressHtml(input)).toBe(expectedOutput);
    });

    it('should replace multiple spaces with a single space', () => {
        const input = '<div>    <p>     Test with     multiple spaces.   </p></div>';
        const expectedOutput = '<div><p> Test with multiple spaces. </p></div>';
        expect(compressHtml(input)).toBe(expectedOutput);
    });

    it('should remove spaces between HTML tags', () => {
        const input = '<div> <p>Test</p> </div>';
        const expectedOutput = '<div><p>Test</p></div>';
        expect(compressHtml(input)).toBe(expectedOutput);
    });

    it('should handle empty input', () => {
        const input = '';
        const expectedOutput = '';
        expect(compressHtml(input)).toBe(expectedOutput);
    });

    it('should handle HTML with only spaces and newlines', () => {
        const input = `
            <div>      
            </div>
        `;
        const expectedOutput = '<div></div>';
        expect(compressHtml(input)).toBe(expectedOutput);
    });
});
