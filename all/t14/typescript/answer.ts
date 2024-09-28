import * as fs from 'fs';
import * as path from 'path';

function findJsonFilesWithKeyword(directory: string, keyword: string): string[] {
    /**
     * Search all JSON files in the specified directory for a given keyword
     * and return a list of filenames that contain the keyword.
     *
     * Args:
     *     directory (str): Path to the directory where JSON files are stored.
     *     keyword (str): Keyword to search for within the JSON files.
     *
     * Returns:
     *     list: A list of filenames (str) of JSON files containing the keyword.
     */
    const matchingFiles: string[] = [];

    function walkDirectory(dir: string): void {
        const files = fs.readdirSync(dir);

        for (const file of files) {
            const filePath = path.join(dir, file);
            const stat = fs.statSync(filePath);

            if (stat.isDirectory()) {
                walkDirectory(filePath);
            } else if (file.endsWith('.json')) {
                try {
                    const data = fs.readFileSync(filePath, 'utf8');
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

    walkDirectory(directory);
    return matchingFiles;
}