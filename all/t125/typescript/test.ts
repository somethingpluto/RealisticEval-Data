describe('compressHTML', () => {
    test('should remove leading and trailing spaces around tags', () => {
        const input: string = '  <div>  <p>Test</p>  </div>  ';
        const expected: string = '<div><p>Test</p></div>';
        expect(compressHTML(input)).toBe(expected);
    });

    test('should replace multiple newlines with a single space', () => {
        const input: string = '<div>\n\n<p>Test</p>\n\n</div>';
        const expected: string = '<div> <p>Test</p> </div>';
        expect(compressHTML(input)).toBe(expected);
    });

    test('should remove unnecessary spaces within text', () => {
        const input: string = '<p>This    is a test</p>';
        const expected: string = '<p>This is a test</p>';
        expect(compressHTML(input)).toBe(expected);
    });

    test('should handle empty strings', () => {
        const input: string = '';
        const expected: string = '';
        expect(compressHTML(input)).toBe(expected);
    });

    test('should process complex nested HTML correctly', () => {
        const input: string = '<div>   <span>    Text <i>    Italic </i> more text </span>   </div>';
        const expected: string = '<div><span>Text <i>Italic</i> more text</span></div>';
        expect(compressHTML(input)).toBe(expected);
    });

    test('should not disrupt content within <pre> and <textarea> tags', () => {
        const input: string = '<pre>\n    function example() {\n        console.log("example");\n    }\n</pre>';
        const expected: string = '<pre>\n    function example() {\n        console.log("example");\n    }\n</pre>'; // assuming no changes in <pre> and <textarea>
        expect(compressHTML(input)).toBe(expected);
    });

    test('should handle HTML with attributes correctly', () => {
        const input: string = '<a href="http://example.com"    title="Example" >Link</a>';
        const expected: string = '<a href="http://example.com" title="Example">Link</a>';
        expect(compressHTML(input)).toBe(expected);
    });
});