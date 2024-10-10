describe('Dataframe to Markdown conversion', () => {
    it('should convert a DataFrame object to a markdown table', () => {
        const df = {
            Name: ['Alice', 'Bob'],
            Age: [25, 30]
        };

        const mdPath = './output.md';

        expect(dataFrameToMarkdown(df, mdPath)).toBe('| Name | Age |\n| --- | --- |\n| Alice | 25 |\n| Bob | 30 |\n');
    });
});