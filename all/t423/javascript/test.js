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
