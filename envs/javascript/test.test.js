import csvParser from 'csv-parser';
import process from 'process';

function readTSVFromStdin() {
    // Create a stream to read from standard input
    const stdinStream = process.stdin;
    let data = [];

    // Set up the CSV parser with tab as the delimiter
    stdinStream
        .setEncoding('utf8')
        .on('data', chunk => {
            const rows = chunk.split('\n').map(row => row.split('\t'));
            data = data.concat(rows);
        })
        .on('end', () => {
            // Process the data after reading is complete
            const processedData = processPaddedData(data);
            console.log(processedData);
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
