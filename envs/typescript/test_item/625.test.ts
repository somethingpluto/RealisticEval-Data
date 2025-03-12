import * as fs from 'fs';
import * as path from 'path';

function readDataFromFile(path: string): (number | string)[] {
  const resolvedPath = path.resolve(path);
  const data: (number | string)[] = [];

  try {
    const content = fs.readFileSync(resolvedPath, 'utf8');
    const lines = content.split(/\r?\n/);

    lines.forEach(line => {
      const trimmedLine = line.trim();
      if (trimmedLine.length === 0) return; // Skip empty lines

      let value: number | string;
      const match = trimmedLine.match(/^(-?\d+\.?\d*)$/);
      if (match) {
        value = parseFloat(match[1]);
        if (Number.isInteger(value)) {
          value = parseInt(match[1], 10);
        }
      } else {
        value = trimmedLine;
      }

      data.push(value);
    });
  } catch (error) {
    throw new Error(`Error reading file at ${resolvedPath}: ${error.message}`);
  }

  return data;
}
import * as fs from 'fs';

describe('Tester', () => {
    const createTestFile = (fileName: string, content: string): void => {
        fs.writeFileSync(fileName, content);
    };

    afterEach(() => {
        // Cleanup: Remove test files after each test
        const testFiles = ['valid_integers.txt', 'valid_floats.txt', 'mixed_data.txt', 'empty_file.txt', 'invalid_data.txt'];
        testFiles.forEach(file => {
            if (fs.existsSync(file)) {
                fs.unlinkSync(file);
            }
        });
    });

    test('read valid integers', () => {
        const filePath = 'valid_integers.txt';
        createTestFile(filePath, '42\n-7\n0\n100\n');
        const result = readDataFromFile(filePath);
        expect(result.length).toBe(4);
        expect(result[0]).toBe(42);
        expect(result[1]).toBe(-7);
        expect(result[2]).toBe(0);
        expect(result[3]).toBe(100);
    });

    test('read valid floats', () => {
        const filePath = 'valid_floats.txt';
        createTestFile(filePath, '3.14\n-0.001\n2.71828\n0.0\n');
        const result = readDataFromFile(filePath);
        expect(result.length).toBe(4);
        expect(result[0]).toBe(3.14);
        expect(result[1]).toBe(-0.001);
        expect(result[2]).toBe(2.71828);
        expect(result[3]).toBe(0.0);
    });

    test('read mixed data', () => {
        const filePath = 'mixed_data.txt';
        createTestFile(filePath, 'Hello\n42\n3.14\nWorld\n-19.99\n');
        const result = readDataFromFile(filePath);
        expect(result.length).toBe(5);
        expect(result[0]).toBe('Hello');
        expect(result[1]).toBe(42);
        expect(result[2]).toBe(3.14);
        expect(result[3]).toBe('World');
        expect(result[4]).toBe(-19.99);
    });

    test('read empty file', () => {
        const filePath = 'empty_file.txt';
        createTestFile(filePath, '');
        const result = readDataFromFile(filePath);
        expect(result.length).toBe(0);
    });

    test('read invalid data', () => {
        const filePath = 'invalid_data.txt';
        createTestFile(filePath, 'Hello\n42a\n3.14.15\nWorld!\n');
        const result = readDataFromFile(filePath);
        expect(result.length).toBe(4);
        expect(result[0]).toBe('Hello');
        expect(result[1]).toBe('42a');
        expect(result[2]).toBe('3.14.15');
        expect(result[3]).toBe('World!');
    });
});
