const fs = require('fs');
const path = require('path');

/**
 * Search all JSON files in the specified directory for a given keyword
 * and return a list of filenames that contain the keyword.
 *
 * @param {string} directory - Path to the directory where JSON files are stored.
 * @param {string} keyword - Keyword to search for within the JSON files.
 * @returns {string[]} - A list of filenames (strings) of JSON files containing the keyword.
 */
function findJsonFilesWithKeyword(directory, keyword) {
    const matchingFiles = [];
    
    function walkDir(currentPath) {
        const files = fs.readdirSync(currentPath);

        for (const file of files) {
            const filePath = path.join(currentPath, file);
            const stat = fs.statSync(filePath);

            if (stat.isDirectory()) {
                walkDir(filePath);
            } else if (file.endsWith('.json')) {
                try {
                    const data = fs.readFileSync(filePath, 'utf-8');
                    const jsonData = JSON.parse(data);
                    if (JSON.stringify(jsonData).includes(keyword)) {
                        matchingFiles.push(file);
                    }
                } catch (e) {
                    console.error(`Error reading ${filePath}: ${e}`);
                }
            }
        }
    }

    walkDir(directory);
    return matchingFiles;
}