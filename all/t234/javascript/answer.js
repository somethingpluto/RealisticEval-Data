const fs = require('fs');
const csvParser = require('csv-parser');
const fastCsv = require('fast-csv');

function appendOrSkipRow(filePath, rowCandidate) {
    return new Promise((resolve, reject) => {
        const firstThreeColumns = rowCandidate.slice(0, 3).join(',');
        let exists = false;

        // Read the CSV file and check for duplicate rows
        fastCsv.parseFile(filePath)
            .on('data', (row) => {
                if (row.slice(0, 3).join(',') === firstThreeColumns) {
                    exists = true;
                }
            })
            .on('end', () => {
                if (!exists) {
                    // Append the new row if it doesn't exist
                    fastCsv.writeToPath(filePath, [rowCandidate], { headers: false, delimiter: ',' })
                        .then(() => resolve())
                        .catch(reject);
                } else {
                    resolve();
                }
            });
    });
}