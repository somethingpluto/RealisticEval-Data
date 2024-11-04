const fs = require('fs');
const path = require('path');
const Papa = require('papaparse');


function findCommonColumns(directory) {
    // List to store the parsed CSV data
    const csvData = [];

    // Iterate through all files in the specified directory
    fs.readdir(directory, (err, files) => {
        if (err) throw err;

        files.forEach(file => {
            if (file.endsWith('.csv')) {
                // Construct the full file path
                const filePath = path.join(directory, file);

                // Read the CSV file synchronously
                fs.readFile(filePath, 'utf8', (err, data) => {
                    if (err) throw err;

                    // Parse the CSV data
                    const parsedData = Papa.parse(data, { header: true });
                    const headers = new Set(parsedData.meta.fields);

                    // Add the headers to the list
                    csvData.push(headers);
                });
            }
        });

        // Wait for all CSV files to be read and parsed
        setTimeout(() => {
            // Use set intersection to find common columns across all CSV files
            if (csvData.length > 0) {
                let commonColumns = new Set(csvData[0]);

                // Intersect with columns of each subsequent CSV file
                csvData.slice(1).forEach(set => {
                    commonColumns = new Set([...commonColumns].filter(x => set.has(x)));
                });

                console.log(Array.from(commonColumns));
            } else {
                // Return an empty array if no CSV files are found
                console.log([]);
            }
        }, 1000); // Wait for all asynchronous reads to complete
    });
}