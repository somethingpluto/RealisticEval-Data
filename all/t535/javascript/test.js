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