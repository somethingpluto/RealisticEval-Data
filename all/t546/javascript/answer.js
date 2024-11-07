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