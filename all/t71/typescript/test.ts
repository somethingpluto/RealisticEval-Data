import { writeFileSync, existsSync, unlinkSync } from 'fs';

describe('readColumns', () => {
    const testFile = 'test_file.txt';

    beforeEach(() => {
        // Setup a temporary directory to use for each test
    });

    afterEach(() => {
        // Clean up the temporary file after each test
        if (existsSync(testFile)) {
            unlinkSync(testFile);
        }
    });

    it('should read a file with a valid structure and numerical data', () => {
        const content = `Line 1
Line 2
/
1.0 2.0 3.0
4.0 5.0 6.0`;

        writeFileSync(testFile, content);

        const result = readColumns(testFile);
        const expectedResult = [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]];
        expect(result).toEqual(expectedResult);
    });

    it('should throw an error if no \'/\' character is found', () => {
        const content = `Line 1
Line 2
Line 3`;

        writeFileSync(testFile, content);

        expect(() => readColumns(testFile)).toThrow('File does not contain \'/\' character');
    });

    it('should handle comments and empty lines correctly', () => {
        const content = `Line 1
/
! This is a comment
1.0 2.0 3.0

4.0 5.0 6.0
! Another comment`;

        writeFileSync(testFile, content);

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

        writeFileSync(testFile, content);

        expect(() => readColumns(testFile)).toThrow();
    });

    it('should throw an error if the file is empty', () => {
        const content = ``;

        writeFileSync(testFile, content);

        expect(() => readColumns(testFile)).toThrow('File does not contain \'/\' character');
    });
});