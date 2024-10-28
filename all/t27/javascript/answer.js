const fs = require('fs');
const path = require('path');

function concatenateJsonArrays(directory) {
    const combinedData = [];

    // Read all files in the directory
    const files = fs.readdirSync(directory);

    // Loop through all files in the directory
    for (const filename of files) {
        // Check if the file is a JSON file
        if (filename.endsWith('.json')) {
            // Construct the full file path
            const filePath = path.join(directory, filename);
            try {
                // Read and parse the JSON file
                const data = JSON.parse(fs.readFileSync(filePath, 'utf-8'));

                // Check if the data is an array
                if (Array.isArray(data)) {
                    combinedData.push(...data);
                } else {
                    console.warn(`Warning: ${filename} does not contain a root-level array.`);
                }
            } catch (error) {
                console.error(`Error reading ${filename}:`, error.message);
            }
        }
    }

    return combinedData;
}