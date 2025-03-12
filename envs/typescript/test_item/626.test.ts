import { readFile } from 'fs/promises';
import { join } from 'path';

async function readFileAndProcessLines(path: string): Promise<string[]> {
  try {
    const fullPath = join(__dirname, path);
    const fileContent = await readFile(fullPath, 'utf8');
    return fileContent.split(/\r?\n/).map(line => line.replace(/\/\/.*$/, ''));
  } catch (error) {
    throw new Error(`Error reading file at path: ${path}`);
  }
}
import fs from 'fs';
import path from 'path';

describe('TestAnswer', () => {
    const testFilePath = path.join(__dirname, 'testFile.txt');

    beforeEach(() => {
        /** Create a temporary file for testing. */
        fs.writeFileSync(testFilePath, '');
    });

    const writeToFile = (content: string) => {
        /** Helper method to write to the test file. */
        fs.writeFileSync(testFilePath, content);
    };

    afterEach(() => {
        /** Cleanup after tests. */
        try {
            fs.unlinkSync(testFilePath);
        } catch (error) {
            // Ignore if the file doesn't exist
        }
    });

    test('normal input', () => {
        /** Test processing of normal input. */
        writeToFile("Line 1\nLine 2 # Comment\nLine 3\n");
        const result = readFileAndProcessLines(testFilePath);
        expect(result).toEqual(["Line 1", "Line 2", "Line 3"]);
    });

    test('only comments', () => {
        /** Test processing when only comments are present. */
        writeToFile("# This is a comment\n# Another comment\n");
        const result = readFileAndProcessLines(testFilePath);
        expect(result).toEqual([]);
    });

    test('empty lines', () => {
        /** Test processing with empty lines. */
        writeToFile("Line 1\n\nLine 2\n\n\nLine 3 # Comment\n");
        const result = readFileAndProcessLines(testFilePath);
        expect(result).toEqual(["Line 1", "Line 2", "Line 3"]);
    });

    test('no inline comments', () => {
        /** Test processing when there are no inline comments. */
        writeToFile("Line 1\nLine 2\nLine 3\n");
        const result = readFileAndProcessLines(testFilePath);
        expect(result).toEqual(["Line 1", "Line 2", "Line 3"]);
    });

    test('only new lines', () => {
        /** Test processing with only new lines. */
        writeToFile("\n\n\n\n");
        const result = readFileAndProcessLines(testFilePath);
        expect(result).toEqual([]);
    });

    test('mixed content', () => {
        /** Test processing with mixed content. */
        writeToFile("Valid line\n# This is a comment\nLine 2\n# Another comment\n\nLine 3 # End of line comment\n");
        const result = readFileAndProcessLines(testFilePath);
        expect(result).toEqual(["Valid line", "Line 2", "Line 3"]);
    });
});
