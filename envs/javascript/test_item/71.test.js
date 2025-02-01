/**
 * Reads numerical columns from a file starting from the line after the last line containing '/'.
 *
 * @param {string} fileName - The name of the file to read.
 * @returns {Array<Array<number>>} - A 2D array containing the numerical data.
 * @throws {Error} - If the file does not contain any '/' character.
 */
function readColumns(fileName) {
    const fs = require('fs');
    const readline = require('readline');

    let lastLineWithSlash = null;
    let numericalData = [];

    const fileStream = fs.createReadStream(fileName);
    const rl = readline.createInterface({
        input: fileStream,
        crlfDelay: Infinity
    });

    rl.on('line', (line) => {
        if (line.includes('/')) {
            lastLineWithSlash = line;
        }
    });

    rl.on('close', () => {
        if (!lastLineWithSlash) {
            throw new Error('File does not contain any "/" character.');
        }

        const linesAfterLastSlash = fs.readFileSync(fileName).toString().split('\n').slice(fs.readFileSync(fileName).toString().split('\n').indexOf(lastLineWithSlash) + 1);
        linesAfterLastSlash.forEach((line) => {
            const numbers = line.trim().split(/\s+/).map(Number);
            if (numbers.length > 0) {
                numericalData.push(numbers);
            }
        });

        return numericalData;
    });
}
describe('TestReadColumns', () => {
    const testFile = 'test_file.txt';

    beforeEach(() => {
        // Setup a temporary directory to use for each test
    });

    afterEach(() => {
        // Clean up the temporary file after each test
        if (fs.existsSync(testFile)) {
            fs.unlinkSync(testFile);
        }
    });

    it('should handle basic functionality', () => {
        const content = `Line 1
Line 2
/
1.0 2.0 3.0
4.0 5.0 6.0`;

        fs.writeFileSync(testFile, content);

        const result = readColumns(testFile);
        const expectedResult = [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]];
        expect(result).toEqual(expectedResult);
    });

    it('should throw an error if no "/" character is found', () => {
        const content = `Line 1
Line 2
Line 3`;

        fs.writeFileSync(testFile, content);

        expect(() => readColumns(testFile)).toThrow('File does not contain \'/\' character');
    });

    it('should handle comments and empty lines', () => {
        const content = `Line 1
/
! This is a comment
1.0 2.0 3.0

4.0 5.0 6.0
! Another comment`;

        fs.writeFileSync(testFile, content);

        const result = readColumns(testFile);
        const expectedResult = [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]];
        expect(result).toEqual(expectedResult);
    });

    it('should throw an error if the number of columns is inconsistent', () => {
        const content = `Line 1
/
1.0 2.0
3.0 4.0
5.0 6.0 7.0`;

        fs.writeFileSync(testFile, content);

        expect(() => readColumns(testFile)).toThrow('File does not contain \'/\' character');
    });

    it('should throw an error if the file is empty', () => {
        const content = ``;

        fs.writeFileSync(testFile, content);

        expect(() => readColumns(testFile)).toThrow('File does not contain \'/\' character');
    });
});
