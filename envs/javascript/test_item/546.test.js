/**
 * Reads tab-separated values (TSV) from standard input and returns a list of rows.
 * 
 * Each row is represented as an array of strings. If rows have unequal lengths,
 * they are padded with empty strings to ensure all rows have the same length.
 * 
 * @returns {Array<Array<string>>} A list of arrays, where each inner array represents a row of data.
 */
function readTSVFromStdin() {
    return new Promise((resolve, reject) => {
        const rows = [];
        let maxLength = 0;

        process.stdin.setEncoding('utf8');

        process.stdin.on('readable', () => {
            let chunk;
            while ((chunk = process.stdin.read()) !== null) {
                const lines = chunk.split('\n');
                for (const line of lines) {
                    const row = line.split('\t');
                    rows.push(row);
                    if (row.length > maxLength) {
                        maxLength = row.length;
                    }
                }
            }
        });

        process.stdin.on('end', () => {
            // Pad rows to ensure all rows have the same length
            for (let i = 0; i < rows.length; i++) {
                while (rows[i].length < maxLength) {
                    rows[i].push('');
                }
            }
            resolve(rows);
        });

        process.stdin.on('error', (err) => {
            reject(err);
        });
    });
}
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
