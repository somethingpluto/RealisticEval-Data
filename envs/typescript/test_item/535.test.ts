// ... (previous code for context)

function compressHtml(html: string): string {
  // ... (existing code)

  // New code to handle CDATA sections
  html = html.replace(/<!--(.*?)-->/g, (match, content) => {
    return content.replace(/\s+/g, ' ').trim();
  });

  // ... (existing code)
}

// ... (rest of the code for context)
describe('compressHtml', () => {
    it('should remove newlines and tabs', () => {
        const input: string = `
            <div>
                <p>Test paragraph.</p>
            </div>
        `;
        const expectedOutput: string = '<div><p>Test paragraph.</p></div>';
        expect(compressHtml(input)).toBe(expectedOutput);
    });

    it('should replace multiple spaces with a single space', () => {
        const input: string = '<div>    <p>     Test with     multiple spaces.   </p></div>';
        const expectedOutput: string = '<div><p> Test with multiple spaces. </p></div>';
        expect(compressHtml(input)).toBe(expectedOutput);
    });

    it('should remove spaces between HTML tags', () => {
        const input: string = '<div> <p>Test</p> </div>';
        const expectedOutput: string = '<div><p>Test</p></div>';
        expect(compressHtml(input)).toBe(expectedOutput);
    });

    it('should handle empty input', () => {
        const input: string = '';
        const expectedOutput: string = '';
        expect(compressHtml(input)).toBe(expectedOutput);
    });

    it('should handle HTML with only spaces and newlines', () => {
        const input: string = `
            <div>      
            </div>
        `;
        const expectedOutput: string = '<div></div>';
        expect(compressHtml(input)).toBe(expectedOutput);
    });
});
