const fs = require('fs');
const path = require('path');

function concatenateJsonArrays(directory) {
    const combinedData = [];

    // Read all files in the directory
    const files = fs.readdirSync(directory);

    files.forEach((filename) => {
        // Check if the file is a JSON file
        if (filename.endsWith('.json')) {
            // Construct the full file path
            const filePath = path.join(directory, filename);
            // Read the JSON file
            const data = JSON.parse(fs.readFileSync(filePath, 'utf-8'));

            // Check if data is an array
            if (Array.isArray(data)) {
                combinedData.push(...data);
            } else {
                console.log(`Warning: ${filename} does not contain a root-level array.`);
            }
        }
    });

    return combinedData;
}