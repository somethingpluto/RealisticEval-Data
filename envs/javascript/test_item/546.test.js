/**
 * Reads tab-separated values (TSV) from standard input and returns a list of rows.
 * 
 * Each row is represented as an array of strings. If rows have unequal lengths,
 * they are padded with empty strings to ensure all rows have the same length.
 * 
 * @returns {Array<Array<string>>} A list of arrays, where each inner array represents a row of data.
 */
function readTSVFromStdin() {
    const readline = require('readline');
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout,
        terminal: false
    });

    let rows = [];
    let maxRowLength = 0;

    return new Promise((resolve, reject) => {
        rl.on('line', (line) => {
            let row = line.split('\t');
            if (row.length > maxRowLength) {
                maxRowLength = row.length;
            }
            rows.push(row);
        }).on('close', () => {
            for (let i = 0; i < rows.length; i++) {
                while (rows[i].length < maxRowLength) {
                    rows[i].push('');
                }
            }
            resolve(rows);
        }).on('error', (err) => {
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
