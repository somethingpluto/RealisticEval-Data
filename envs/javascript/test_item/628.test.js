const fs = require('fs');
const readline = require('readline');

/**
 * Modifies a specific line in the given file.
 *
 * @param {string} filePath - The path of the file to be modified.
 * @param {number} lineNumber - The line number to be modified (1-based index).
 * @param {string} newValue - The new value to update the line with.
 * @returns {void}
 */
function modifyLineInFile(filePath, lineNumber, newValue) {
    const tempFilePath = `${filePath}.tmp`;
    const readStream = fs.createReadStream(filePath);
    const writeStream = fs.createWriteStream(tempFilePath);
    const rl = readline.createInterface({
        input: readStream,
        output: writeStream,
        terminal: false
    });

    let currentLineNumber = 1;

    rl.on('line', (line) => {
        if (currentLineNumber === lineNumber) {
            writeStream.write(`${newValue}\n`);
        } else {
            writeStream.write(`${line}\n`);
        }
        currentLineNumber++;
    });

    rl.on('close', () => {
        fs.renameSync(tempFilePath, filePath);
    });
}
const fs = require('fs');
const path = require('path');


describe('TestAnswer', () => {
    const TEST_FILE = path.join(__dirname, 'testFile.txt');

    // Setup: Create a test file with initial content before each test
    beforeEach(() => {
        fs.writeFileSync(TEST_FILE, "Line 1\nLine 2\nLine 3\n");
    });

    // Teardown: Clean up the test file after each test
    afterEach(() => {
        try {
            fs.unlinkSync(TEST_FILE);
        } catch (err) {
            // If the file does not exist, we can safely ignore the error
        }
    });

    test('modify line success', () => {
        modifyLineInFile(TEST_FILE, 2, "Updated Line 2");
        const lines = fs.readFileSync(TEST_FILE, 'utf-8').split('\n');
        expect(lines[0]).toBe("Line 1");
        expect(lines[1]).toBe("Updated Line 2");
        expect(lines[2]).toBe("Line 3");
    });

    test('modify first line', () => {
        modifyLineInFile(TEST_FILE, 1, "Updated Line 1");
        const lines = fs.readFileSync(TEST_FILE, 'utf-8').split('\n');
        expect(lines[0]).toBe("Updated Line 1");
        expect(lines[1]).toBe("Line 2");
        expect(lines[2]).toBe("Line 3");
    });

    test('modify last line', () => {
        modifyLineInFile(TEST_FILE, 3, "Updated Line 3");
        const lines = fs.readFileSync(TEST_FILE, 'utf-8').split('\n');
        expect(lines[0]).toBe("Line 1");
        expect(lines[1]).toBe("Line 2");
        expect(lines[2]).toBe("Updated Line 3");
    });

    test('modify non-existent line', () => {
        expect(() => {
            modifyLineInFile(TEST_FILE, 4, "Should Fail");
        }).toThrow();
    });

    test('modify negative line number', () => {
        expect(() => {
            modifyLineInFile(TEST_FILE, 0, "Should Fail");
        }).toThrow();
    });
});
