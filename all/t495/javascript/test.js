describe('TestFilterContentWithContext', () => {
    describe('Single Keyword Match', () => {
        it('should correctly filter content for a single keyword with context lines', () => {
            const content = `Line one.
            This line contains a keyword.
            Line three.`;
            const keywords = ['keyword'];
            const expectedOutput = `Line one.
            This line contains a keyword.
            Line three.`;
            const result = filterContentWithContext(content, keywords, 1, 1);
            expect(result.trim()).toEqual(expectedOutput.trim());
        });
    });

    describe('No Keyword Match', () => {
        it('should return an empty string when no keywords match', () => {
            const content = `Line one.
            Line two.
            Line three.`;
            const keywords = ['missing'];
            const expectedOutput = '';
            const result = filterContentWithContext(content, keywords, 1, 1);
            expect(result.trim()).toEqual(expectedOutput);
        });
    });

    describe('Lines Before and After', () => {
        it('should correctly include context lines', () => {
            const content = `Line one.
            This line contains a keyword.
            Line three.
            Line four.
            Line five.`;
            const keywords = ['keyword'];
            const expectedOutput = `Line one.
            This line contains a keyword.
            Line three.`;
            const result = filterContentWithContext(content, keywords, 1, 1);
            expect(result.trim()).toEqual(expectedOutput.trim());
        });
    });
});