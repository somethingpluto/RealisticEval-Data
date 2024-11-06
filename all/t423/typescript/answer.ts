import fs from 'fs';

function writeUniqueLineToFile(filename: string, lineContent: string): void {
    // Check if the lineContent already exists in the file
    fs.readFile(filename, 'utf8', (err, data) => {
        if (err) {
            if (err.code === 'ENOENT') {
                // File does not exist, so we can directly write the line
                appendLineToFile(filename, lineContent);
            } else {
                console.error(`Error reading file: ${err}`);
            }
            return;
        }

        if (data.includes(lineContent)) {
            console.log(`Line '${lineContent}' already exists in '${filename}'. Not writing again.`);
            return;
        }

        // If lineContent is not found, append it to the file
        appendLineToFile(filename, lineContent);
    });
}

function appendLineToFile(filename: string, lineContent: string): void {
    fs.appendFile(filename, lineContent + '\n', (err) => {
        if (err) {
            console.error(`Error writing to file: ${err}`);
            return;
        }
        console.log(`Line '${lineContent}' successfully written to '${filename}'.`);
    });
}