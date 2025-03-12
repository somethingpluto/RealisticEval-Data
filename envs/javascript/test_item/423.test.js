const fs = require('fs');
const readline = require('readline');

/**
 * Writes a line to a text file only if the line with the same content does not already exist.
 * 
 * @param {string} filename - The name of the file to write to.
 * @param {string} lineContent - The content of the line to write.
 */
function writeUniqueLineToFile(filename, lineContent) {
    // Check if the file exists
    fs.access(filename, fs.constants.F_OK, (err) => {
        if (err) {
            // If the file does not exist, create it and write the line
            fs.writeFile(filename, lineContent + '\n', (err) => {
                if (err) throw err;
            });
            return;
        }

        // If the file exists, check if the line already exists
        const fileStream = fs.createReadStream(filename);
        const rl = readline.createInterface({
            input: fileStream,
            crlfDelay: Infinity
        });

        let lineExists = false;

        rl.on('line', (line) => {
            if (line === lineContent) {
                lineExists = true;
                rl.close();
            }
        });

        rl.on('close', () => {
            if (!lineExists) {
                // Append the line to the file if it does not exist
                fs.appendFile(filename, lineContent + '\n', (err) => {
                    if (err) throw err;
                });
            }
        });
    });
}
const fs = require('fs');
const path = require('path');
describe('TestWriteUniqueLineToFile', () => {
    const filename = 'test_file.txt';

    beforeAll(() => {
        // Setup: create a temporary file for testing.
        fs.writeFile(filename, '', (err) => {
            if (err) {
                console.error(`Error creating file: ${err}`);
            }
        });
    });

    afterAll(() => {
        // Cleanup: remove the temporary file after all tests.
        fs.unlink(filename, (err) => {
            if (err) {
                console.error(`Error removing file: ${err}`);
            }
        });
    });

    test('Writing a new line to an empty file', () => {
        const lineContent = "First unique line.";
        writeUniqueLineToFile(filename, lineContent);

        return new Promise((resolve) => {
            setTimeout(() => {
                fs.readFile(filename, 'utf8', (err, data) => {
                    if (err) {
                        console.error(`Error reading file: ${err}`);
                        resolve(false);
                    } else {
                        expect(data).toContain(lineContent);
                        resolve(true);
                    }
                });
            }, 100); // Allow time for the asynchronous write to complete
        });
    });

    test('Attempting to write a duplicate line', () => {
        const lineContent = "First unique line.";
        writeUniqueLineToFile(filename, lineContent);
        writeUniqueLineToFile(filename, lineContent);

        return new Promise((resolve) => {
            setTimeout(() => {
                fs.readFile(filename, 'utf8', (err, data) => {
                    if (err) {
                        console.error(`Error reading file: ${err}`);
                        resolve(false);
                    } else {
                        expect(data.trim().split('\n').filter(line => line === lineContent).length).toBe(1);
                        resolve(true);
                    }
                });
            }, 100); // Allow time for the asynchronous write to complete
        });
    });

    test('Writing multiple unique lines', () => {
        const lines = ["First unique line.", "Second unique line.", "Third unique line."];

        lines.forEach(line => {
            writeUniqueLineToFile(filename, line);
        });

        return new Promise((resolve) => {
            setTimeout(() => {
                fs.readFile(filename, 'utf8', (err, data) => {
                    if (err) {
                        console.error(`Error reading file: ${err}`);
                        resolve(false);
                    } else {
                        lines.forEach(line => {
                            expect(data).toContain(line);
                        });
                        resolve(true);
                    }
                });
            }, 100); // Allow time for the asynchronous write to complete
        });
    });

    test('Writing an empty line, should not write', () => {
        const lineContent = "";
        writeUniqueLineToFile(filename, lineContent);

        return new Promise((resolve) => {
            setTimeout(() => {
                fs.readFile(filename, 'utf8', (err, data) => {
                    if (err) {
                        console.error(`Error reading file: ${err}`);
                        resolve(false);
                    } else {
                        expect(data.trim()).toBe("");
                        resolve(true);
                    }
                });
            }, 100); // Allow time for the asynchronous write to complete
        });
    });
});
