import * as fs from 'fs';
import * as path from 'path';

function concatenateJsonArrays(directory: string): any[] {
    const combinedData: any[] = [];

    // Get all the files in the directory
    const files = fs.readdirSync(directory);

    for (const filename of files) {
        // Check if the file is a JSON file
        if (filename.endsWith('.json')) {
            // Construct the full file path
            const filePath = path.join(directory, filename);
            // Read and parse the JSON file
            try {
                const fileContent = fs.readFileSync(filePath, 'utf-8');
                const data = JSON.parse(fileContent);

                // Check if the data is an array
                if (Array.isArray(data)) {
                    combinedData.push(...data);
                } else {
                    console.warn(`Warning: ${filename} does not contain a root-level array.`);
                }
            } catch (error) {
                console.error(`Error reading or parsing ${filename}:`, error);
            }
        }
    }

    return combinedData;
}