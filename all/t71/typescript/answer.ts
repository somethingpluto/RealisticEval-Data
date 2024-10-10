import * as fs from 'fs';
import { parse } from 'csv-parse';

function readColumns(fileName: string): Promise<Array<Array<number>>> {
    return new Promise((resolve, reject) => {
        let foundDivider = false;
        const data: Array<Array<number>> = [];

        fs.createReadStream(fileName)
            .pipe(parse({ delimiter: ',', columns: true }))
            .on('data', (row) => {
                if (!foundDivider && !row['/']) {
                    return; // Skip lines until we find the divider
                }
                foundDivider = true;

                // Convert each column value to number and push to data array
                const rowValues = Object.values(row).map(value => parseFloat(value));
                data.push(rowValues);
            })
            .on('end', () => {
                resolve(data);
            })
            .on('error', (err) => {
                reject(err);
            });
    });
}