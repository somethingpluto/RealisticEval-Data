describe('TestReadTsvFromStdin', () => {
    beforeEach(() => {
        // Reset the standard input stream before each test
        process.stdin.setEncoding('utf8');
    });

    test('test basic TSV input', () => {
        const mockStdin = 'col1\tcol2\tcol3\nval1\tval2\tval3\n';
        process.stdin.emit('data', mockStdin);
        process.stdin.emit('end');

        const expectedOutput = [['col1', 'col2', 'col3'], ['val1', 'val2', 'val3']];
        expect(readTSVFromStdin()).toEqual(expectedOutput);
    });

    test('test single column', () => {
        const mockStdin = 'col1\nval1\nval2\n';
        process.stdin.emit('data', mockStdin);
        process.stdin.emit('end');

        const expectedOutput = [['col1'], ['val1'], ['val2']];
        expect(readTSVFromStdin()).toEqual(expectedOutput);
    });
});