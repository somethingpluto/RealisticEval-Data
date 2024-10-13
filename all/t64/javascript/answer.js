const fs = require('fs');
const path = require('path');
const csvParser = require('csv-parser');

function csvToSqlInsert(csvFilePath) {
    // Extract the table name from the CSV file name, removing the suffix
    const tableName = path.splitext(path.basename(csvFilePath))[0];

    // Open the CSV file and read its contents
    const results = [];
    let headers = [];

    fs.createReadStream(csvFilePath)
        .on('data', (row) => {
            if (!headers.length) {
                headers = Object.keys(row);
                return;
            }

            const values = [];
            for (const [key, value] of Object.entries(row)) {
                // Handle different types of values (e.g., strings, numbers)
                if (!isNaN(value)) {  // If value is a number, no quotes needed
                    values.push(value);
                } else {  // Assume it's a string otherwise
                    const escapedValue = value.replace(/'/g, "''");  // Escape single quotes
                    values.push(`'${escapedValue}'`);  // Use double quotes outside
                }
            }

            // Join column names and values to form an INSERT statement
            const insertStatement = `INSERT INTO ${tableName} (${headers.join(', ')}) VALUES (${values.join(', ')});`;
            results.push(insertStatement);
        })
        .on('end', () => {
            // Combine all insert statements into a single output
            console.log(results.join('\n'));
        })
        .pipe(csvParser());
}