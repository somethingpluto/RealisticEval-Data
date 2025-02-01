const fs = require('fs');

/**
 * Finds and replaces text in a specified file.
 *
 * @param {string} filePath - The path to the file.
 * @param {string} searchString - The string to search for.
 * @param {string} replaceString - The string to replace with.
 * @throws {Error} If an I/O error occurs reading from the file or writing to the file.
 */
function findAndReplaceInFile(filePath, searchString, replaceString) {
  // Read the file content
  fs.readFile(filePath, 'utf8', (err, data) => {
    if (err) {
      throw new Error(`Error reading file: ${err.message}`);
    }

    // Replace the search string with the replace string
    const modifiedData = data.replace(searchString, replaceString);

    // Write the modified content back to the file
    fs.writeFile(filePath, modifiedData, 'utf8', (err) => {
      if (err) {
        throw new Error(`Error writing to file: ${err.message}`);
      }
      console.log('Text replaced successfully.');
    });
  });
}
const fs = require('fs');
const path = require('path');

describe('TestFindAndReplace', () => {
    let tempDir;

    beforeAll(() => {
        // Create a temporary directory for the tests
        tempDir = path.join(__dirname, 'temp');
        fs.mkdirSync(tempDir, { recursive: true });
    });

    afterAll(() => {
        // Remove the temporary directory after tests
        fs.readdirSync(tempDir).forEach(file => {
            fs.unlinkSync(path.join(tempDir, file));
        });
        fs.rmdirSync(tempDir);
    });

    // Test case 1: Basic find and replace
    test('find and replace basic', () => {
        const filePath = path.join(tempDir, 'testfile.txt');
        fs.writeFileSync(filePath, 'Hello World\nGoodbye World\n');

        findAndReplaceInFile(filePath, 'World', 'Java');

        const result = fs.readFileSync(filePath, 'utf-8').split('\n');
        expect(result).toEqual(['Hello Java', 'Goodbye Java', '']);
    });

    // Test case 2: No occurrences of the search string
    test('find and replace no occurrences', () => {
        const filePath = path.join(tempDir, 'testfile.txt');
        fs.writeFileSync(filePath, 'Hello World\nGoodbye World\n');

        findAndReplaceInFile(filePath, 'Python', 'Java');

        const result = fs.readFileSync(filePath, 'utf-8').split('\n');
        expect(result).toEqual(['Hello World', 'Goodbye World', '']);
    });

    // Test case 3: Multiple occurrences in a single line
    test('find and replace multiple occurrences', () => {
        const filePath = path.join(tempDir, 'testfile.txt');
        fs.writeFileSync(filePath, 'Hello World World\nGoodbye World\n');

        findAndReplaceInFile(filePath, 'World', 'Java');

        const result = fs.readFileSync(filePath, 'utf-8').split('\n');
        expect(result).toEqual(['Hello Java Java', 'Goodbye Java', '']);
    });

    // Test case 4: Replace with an empty string
    test('find and replace with empty string', () => {
        const filePath = path.join(tempDir, 'testfile.txt');
        fs.writeFileSync(filePath, 'Hello World\nGoodbye World\n');

        findAndReplaceInFile(filePath, 'World', '');

        const result = fs.readFileSync(filePath, 'utf-8').split('\n');
        expect(result).toEqual(['Hello ', 'Goodbye ', '']);
    });

    // Test case 5: Empty file
    test('find and replace empty file', () => {
        const filePath = path.join(tempDir, 'testfile.txt');
        fs.writeFileSync(filePath, '\n');

        findAndReplaceInFile(filePath, 'World', 'Java');

        const result = fs.readFileSync(filePath, 'utf-8').split('\n');
        expect(result).toEqual(['', '']);
    });
});
