import { readFile, writeFile } from 'fs/promises';
import { resolve } from 'path';

// ...

async function modifyLineInFile(filePath: string, lineNumber: number, newValue: string): Promise<void> {
  try {
    const resolvedPath = resolve(filePath);
    const fileContent = await readFile(resolvedPath, 'utf8');
    const lines = fileContent.split('\n');
    if (lineNumber > 1 && lineNumber <= lines.length) {
      lines[lineNumber - 1] = newValue;
    } else {
      throw new Error('Invalid line number.');
    }
    const updatedContent = lines.join('\n');
    await writeFile(resolvedPath, updatedContent, 'utf8');
  } catch (error) {
    console.error('An error occurred:', error);
  }
}

// ...
import * as fs from 'fs';

describe('TestAnswer', () => {
    const TEST_FILE = 'testFile.txt';

    beforeEach(() => {
        // Create a test file with initial content
        fs.writeFileSync(TEST_FILE, 'Line 1\nLine 2\nLine 3\n');
    });

    afterEach(() => {
        // Clean up the test file after each test
        try {
            fs.unlinkSync(TEST_FILE);
        } catch (err) {
            // File might already be deleted
        }
    });

    test('modify line success', () => {
        modifyLineInFile(TEST_FILE, 2, 'Updated Line 2');
        const lines = fs.readFileSync(TEST_FILE, 'utf-8').split('\n');
        expect(lines[0]).toBe('Line 1');
        expect(lines[1]).toBe('Updated Line 2');
        expect(lines[2]).toBe('Line 3');
    });

    test('modify first line', () => {
        modifyLineInFile(TEST_FILE, 1, 'Updated Line 1');
        const lines = fs.readFileSync(TEST_FILE, 'utf-8').split('\n');
        expect(lines[0]).toBe('Updated Line 1');
        expect(lines[1]).toBe('Line 2');
        expect(lines[2]).toBe('Line 3');
    });

    test('modify last line', () => {
        modifyLineInFile(TEST_FILE, 3, 'Updated Line 3');
        const lines = fs.readFileSync(TEST_FILE, 'utf-8').split('\n');
        expect(lines[0]).toBe('Line 1');
        expect(lines[1]).toBe('Line 2');
        expect(lines[2]).toBe('Updated Line 3');
    });

    test('modify non-existent line', () => {
        expect(() => {
            modifyLineInFile(TEST_FILE, 4, 'Should Fail');
        }).toThrow();
    });

    test('modify negative line number', () => {
        expect(() => {
            modifyLineInFile(TEST_FILE, 0, 'Should Fail');
        }).toThrow();
    });
});
