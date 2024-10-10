import * as fs from 'fs';
import { parse } from 'csv';

function tsvToJsonl(tsvFile: string, jsonlFile: string): void {
    /**
     * Convert tsv file to jsonl file
     *
     * @param tsvFile - Path to the TSV file
     * @param jsonlFile - Path to the JSONL file
     */
    
    const readStream = fs.createReadStream(tsvFile);
    const writeStream = fs.createWriteStream(jsonlFile);

    readStream.pipe(parse({ delimiter: '\t' }))
        .on('data', (row) => {
            const jsonString = JSON.stringify(row);
            writeStream.write(`${jsonString}\n`);
        })
        .on('end', () => {
            console.log(`Conversion complete. JSONL file saved at ${jsonlFile}`);
            writeStream.end();
        })
        .on('error', (err) => {
            console.error('Error during conversion:', err);
            writeStream.destroy(err);
        });
}