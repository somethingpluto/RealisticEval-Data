const fs = require('fs');

function readMappingFile(mappingFilePath) {
    /**
     * Read a mapping file and return an array of tuples with compiled regex and replacement strings.
     *
     * @param {string} mappingFilePath - Path to the file containing regex mappings.
     * @returns {Array} - Each tuple contains a compiled regex object and a corresponding replacement string.
     * @throws {Error} - Throws an error if the mapping file does not exist or if any line in the file does not contain exactly one comma.
     *
     * Example of file format:
     * 'old_pattern1','new_word1'
     * 'old_pattern2','new_word2'
     */

    const mappings = [];

    try {
        fs.readFile(mappingFilePath, 'utf8', (err, data) => {
            if (err) {
                throw new Error(`Unable to find the specified file: ${mappingFilePath}`);
            }

            const lines = data.split('\n');
            lines.forEach(line => {
                if (!line.includes(',')) {
                    throw new Error("Each line must contain exactly one comma separating the pattern and the replacement.");
                }

                const [oldPattern, newWord] = line.trim().split(',', 1);
                const trimmedOldPattern = oldPattern.trim().replace(/^'|'$/g, '');
                const trimmedNewWord = newWord.trim().replace(/^'|'$/g, '');
                mappings.push([new RegExp(trimmedOldPattern), trimmedNewWord]);
            });
        });
    } catch (error) {
        throw error;
    }

    return mappings;
}

