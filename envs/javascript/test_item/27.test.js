const fs = require('fs');
const path = require('path');

/**
 * Concatenate the root-level array JSON files in the specified directory.
 * 
 * @param {string} directory - The directory path.
 * @returns {Array} Merged array of JSON objects.
 */
function concatenateJsonArrays(directory) {
    // Initialize an empty array to hold the merged results
    let mergedArray = [];

    // Read the directory contents
    const files = fs.readdirSync(directory);

    // Iterate over each file in the directory
    files.forEach(file => {
        // Construct the full file path
        const filePath = path.join(directory, file);

        // Check if the file is a JSON file
        if (path.extname(file) === '.json') {
            try {
                // Read the file content
                const fileContent = fs.readFileSync(filePath, 'utf8');

                // Parse the JSON content
                const jsonArray = JSON.parse(fileContent);

                // Check if the parsed content is an array
                if (Array.isArray(jsonArray)) {
                    // Concatenate the array to the merged array
                    mergedArray = mergedArray.concat(jsonArray);
                }
            } catch (error) {
                // Handle any errors (e.g., invalid JSON)
                console.error(`Error reading or parsing file ${file}:`, error);
            }
        }
    });

    // Return the merged array
    return mergedArray;
}
const fs = require('fs');
const path = require('path');
describe('concatenateJsonArrays', () => {
    const testDir = 'test_json';

    beforeAll(() => {
        // Set up test directory and JSON files
        fs.mkdirSync(testDir, { recursive: true });
        fs.writeFileSync(path.join(testDir, 'array1.json'), JSON.stringify([1, 2, 3]));
        fs.writeFileSync(path.join(testDir, 'array2.json'), JSON.stringify(['a', 'b', 'c']));
        fs.writeFileSync(path.join(testDir, 'not_array.json'), JSON.stringify({ key: 'value' }));
        fs.writeFileSync(path.join(testDir, 'empty.json'), JSON.stringify([]));
        fs.writeFileSync(path.join(testDir, 'non_json.txt'), "This is not a JSON file.");
    });

    afterAll(() => {
        // Clean up: Remove created files and directory
        fs.readdirSync(testDir).forEach(file => {
            fs.unlinkSync(path.join(testDir, file));
        });
        fs.rmdirSync(testDir);
    });

    test('concatenate valid JSON arrays', () => {
        const result = concatenateJsonArrays(testDir);
        expect(result).toEqual(expect.arrayContaining([1, 2, 3, 'a', 'b', 'c']));
    });

    test('ignore non-array JSON', () => {
        const result = concatenateJsonArrays(testDir);
        expect(result).not.toContain('key');
    });

    test('ignore non-JSON files', () => {
        const result = concatenateJsonArrays(testDir);
        expect(result).not.toContain("This is not a JSON file.");
    });

    test('handle empty arrays', () => {
        const result = concatenateJsonArrays(testDir);
        expect(result).not.toContain([]);
    });

    test('empty directory', () => {
        const emptyDir = 'empty_test_json';
        fs.mkdirSync(emptyDir, { recursive: true });
        const result = concatenateJsonArrays(emptyDir);
        expect(result).toEqual([]);
        fs.rmdirSync(emptyDir);
    });
});

