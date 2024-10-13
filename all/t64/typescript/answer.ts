import * as fs from 'fs';
import * as path from 'path';
import * as csvParser from 'csv-parser';

function csvToSqlInsert(csvFilePath: string): string {
    // Extract the table name from the CSV file name, removing the suffix
    const tableName = path.basename(csvFilePath, path.extname(csvFilePath));

    // Initialize an array to store the SQL insert statements
    let insertStatements: string[] = [];

    // Read the CSV file
    fs.createReadStream(csvFilePath)
        .pipe(csvParser())
        .on('data', (row: any) => {
            // Skip the header row
            if (!insertStatements.length) {
                return;
            }

            // Prepare the values for the SQL insert statement
            const values = Object.values(row).map(value => {
                if (!isNaN(Number(value))) {
                    return value; // If value is a number, no quotes needed
                } else {
                    // Escape single quotes and wrap in double quotes
                    return `'${value.replace(/'/g, "''")}'`;
                }
            });

            // Form the SQL insert statement
            const headers = Object.keys(row);
            const insertStatement = `INSERT INTO ${tableName} (${headers.join(', ')}) VALUES (${values.join(', ')});`;
            insertStatements.push(insertStatement);
        })
        .on('end', () => {
            // Combine all insert statements into a single output
            console.log(insertStatements.join('\n'));
        });
}
