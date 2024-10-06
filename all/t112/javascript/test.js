describe('convertHtmlHeadingsToMarkdown', () => {
    test('should convert <h1> to #', () => {
        const input = '<h1>This is a Heading 1</h1>';
        const output = '# This is a Heading 1';
        expect(convertHtmlHeadingsToMarkdown(input)).toBe(output);
    });

    test('should convert <h2> to ##', () => {
        const input = '<h2>This is a Heading 2</h2>';
        const output = '## This is a Heading 2';
        expect(convertHtmlHeadingsToMarkdown(input)).toBe(output);
    });

    test('should convert <h3> to ###', () => {
        const input = '<h3>This is a Heading 3</h3>';
        const output = '### This is a Heading 3';
        expect(convertHtmlHeadingsToMarkdown(input)).toBe(output);
    });

    test('should convert <h4> to ####', () => {
        const input = '<h4>This is a Heading 4</h4>';
        const output = '#### This is a Heading 4';
        expect(convertHtmlHeadingsToMarkdown(input)).toBe(output);
    });

    test('should convert <h5> to #####', () => {
        const input = '<h5>This is a Heading 5</h5>';
        const output = '##### This is a Heading 5';
        expect(convertHtmlHeadingsToMarkdown(input)).toBe(output);
    });

    test('should convert <h6> to ######', () => {
        const input = '<h6>This is a Heading 6</h6>';
        const output = '###### This is a Heading 6';
        expect(convertHtmlHeadingsToMarkdown(input)).toBe(output);
    });

});