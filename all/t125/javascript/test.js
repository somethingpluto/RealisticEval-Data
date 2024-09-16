describe('compressHTML', () => {
    test('removes unnecessary spaces around tags', () => {
        const html = '   <div>   Content  </div>   ';
        const expected = '<div>Content</div>';
        expect(compressHTML(html)).toBe(expected);
    });

    test('preserves content inside <pre> tags', () => {
        const html = '<pre>    function hello() {\n      console.log("Hello, world!");\n    }    </pre>';
        const expected = '<pre>    function hello() {\n      console.log("Hello, world!");\n    }    </pre>';
        expect(compressHTML(html)).toBe(expected);
    });

    test('removes newlines and spaces starting a newline', () => {
        const html = 'Line 1\n   Line 2\r\n Line 3\r   Line 4';
        const expected = 'Line 1Line 2Line 3Line 4';
        expect(compressHTML(html)).toBe(expected);
    });


    test('handles empty and whitespace-only strings correctly', () => {
        expect(compressHTML('')).toBe('');
        expect(compressHTML('   \n\r  ')).toBe('');
    });
});
