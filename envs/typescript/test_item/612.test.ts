import { promises as fs } from 'fs';
import { join } from 'path';
import { createWriteStream } from 'fs';
import { Transform } from 'stream';

// ... (rest of the existing function)

// New code starts here
const chunkSize = 1024 * 1024; // 1MB chunks
const tempFilePath = join(__dirname, `${filePath}.tmp`);

// Create a writable stream to the temporary file
const writeStream = createWriteStream(tempFilePath);

// Create a transform stream to handle the find and replace operation
const transformStream = new Transform({
  transform(chunk, encoding, callback) {
    const data = chunk.toString();
    const replacedData = data.replace(new RegExp(searchString, 'g'), replaceString);
    this.push(replacedData);
    callback();
  }
});

// Read the file in chunks, process each chunk, and write to the temporary file
fs.createReadStream(filePath)
  .pipe(transformStream)
  .pipe(writeStream)
  .on('finish', async () => {
    try {
      await fs.rename(tempFilePath, filePath);
    } catch (error) {
      throw new Error(`Failed to rename temporary file: ${error}`);
    }
  })
  .on('error', (error) => {
    throw new Error(`An error occurred: ${error}`);
  });
// New code ends here
import * as fs from 'fs';
import * as path from 'path';

describe('TestFindAndReplace', () => {
    const tempDir = path.join(__dirname, 'temp');

    beforeAll(() => {
        // Create a temporary directory for the tests
        fs.mkdirSync(tempDir, { recursive: true });
    });

    afterAll(() => {
        // Remove the temporary directory after tests
        fs.rmdirSync(tempDir, { recursive: true });
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
        expect(result).toEqual(['']);
    });
});
