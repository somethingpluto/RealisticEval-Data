describe('removeTripleBackticks', () => {
    it('should remove triple backticks from each string in the list', () => {
        const input = ['This is ```a test``', 'Another ```string``` here'];
        const expectedOutput = ['This is a test', 'Another string here'];

        const result = removeTripleBackticks(input);

        expect(result).toEqual(expectedOutput);
    });

    it('should handle an empty array', () => {
        const input: string[] = [];
        const expectedOutput: string[] = [];

        const result = removeTripleBackticks(input);

        expect(result).toEqual(expectedOutput);
    });

    it('should not modify strings without triple backticks', () => {
        const input = ['No triple backticks here', 'Neither do these'];
        const expectedOutput = ['No triple backticks here', 'Neither do these'];

        const result = removeTripleBackticks(input);

        expect(result).toEqual(expectedOutput);
    });
});