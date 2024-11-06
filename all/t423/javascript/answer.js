import fs from 'fs'

function writeUniqueLineToFile(filename, lineContent) {
    /**
     * Writes a line to a text file only if the line with the same content does not already exist.
     *
     * @param {string} filename - The name of the file to write to.
     * @param {string} lineContent - The content of the line to write.
     */

    // Check if the lineContent already exists in the file
    fs.readFile(filename, 'utf8', (err, data) => {
        if (err && err.code === 'ENOENT') {
            // File does not exist, so we can directly write the line
            appendLineToFile(filename, lineContent);
        } else if (err) {
            console.error(`Error reading file: ${err}`);
        } else {
            if (data.includes(lineContent)) {
                console.log(`Line '${lineContent}' already exists in '${filename}'. Not writing again.`);
            } else {
                appendLineToFile(filename, lineContent);
            }
        }
    });
}

function appendLineToFile(filename, lineContent) {
    fs.appendFile(filename, lineContent + '\n', (err) => {
        if (err) {
            console.error(`Error writing to file: ${err}`);
        } else {
            console.log(`Line '${lineContent}' successfully written to '${filename}'.`);
        }
    });
}