/**
 * Reads data from a specified file and determines the type of each line.
 * This function processes each line of the specified file and attempts to convert it
 * into either an integer, a floating-point number, or a string.
 *
 * @param {string} path - The path to the file to be read. The file should exist and be accessible for reading.
 * @returns {Array<number|string>} - A list containing the converted values of each line in the file. Each element
 *                                    can be a number (int or float) or a string, depending on the content of the line.
 * @throws {Error} If an error occurs while reading the file.
 */
function readDataFromFile(path) {
    const fs = require('fs');
    const readline = require('readline');

    const lines = [];
    const fileStream = fs.createReadStream(path);
    const rl = readline.createInterface({
        input: fileStream,
        crlfDelay: Infinity
    });

    rl.on('line', (line) => {
        let value;
        if (!isNaN(line) && line.indexOf('.') === -1) {
            value = parseInt(line, 10);
        } else if (!isNaN(line)) {
            value = parseFloat(line);
        } else {
            value = line;
        }
        lines.push(value);
    });

    return new Promise((resolve, reject) => {
        rl.on('close', () => {
            resolve(lines);
        });

        rl.on('error', (err) => {
            reject(err);
        });
    });
}
const fs = require('fs');
const path = require('path');

describe('Tester', () => {
    // Helper function to create a test file
    const createTestFile = (fileName, content) => {
        fs.writeFileSync(fileName, content);
    };

    afterEach(() => {
        // Cleanup: Remove any test files created during tests
        const testFiles = [
            "valid_integers.txt",
            "valid_floats.txt",
            "mixed_data.txt",
            "empty_file.txt",
            "invalid_data.txt"
        ];
        testFiles.forEach(file => {
            if (fs.existsSync(file)) {
                fs.unlinkSync(file);
            }
        });
    });

    test('read valid integers', () => {
        const filePath = "valid_integers.txt";
        createTestFile(filePath, "42\n-7\n0\n100\n");
        const result = readDataFromFile(filePath);
        expect(result.length).toBe(4);
        expect(result[0]).toBe(42);
        expect(result[1]).toBe(-7);
        expect(result[2]).toBe(0);
        expect(result[3]).toBe(100);
    });

    test('read valid floats', () => {
        const filePath = "valid_floats.txt";
        createTestFile(filePath, "3.14\n-0.001\n2.71828\n0.0\n");
        const result = readDataFromFile(filePath);
        expect(result.length).toBe(4);
        expect(result[0]).toBe(3.14);
        expect(result[1]).toBe(-0.001);
        expect(result[2]).toBe(2.71828);
        expect(result[3]).toBe(0.0);
    });

    test('read mixed data', () => {
        const filePath = "mixed_data.txt";
        createTestFile(filePath, "Hello\n42\n3.14\nWorld\n-19.99\n");
        const result = readDataFromFile(filePath);
        expect(result.length).toBe(5);
        expect(result[0]).toBe("Hello");
        expect(result[1]).toBe(42);
        expect(result[2]).toBe(3.14);
        expect(result[3]).toBe("World");
        expect(result[4]).toBe(-19.99);
    });

    test('read empty file', () => {
        const filePath = "empty_file.txt";
        createTestFile(filePath, "");
        const result = readDataFromFile(filePath);
        expect(result.length).toBe(0);
    });

    test('read invalid data', () => {
        const filePath = "invalid_data.txt";
        createTestFile(filePath, "Hello\n42a\n3.14.15\nWorld!\n");
        const result = readDataFromFile(filePath);
        expect(result.length).toBe(4);
        expect(result[0]).toBe("Hello");
        expect(result[1]).toBe("42a");
        expect(result[2]).toBe("3.14.15");
        expect(result[3]).toBe("World!");
    });
});
