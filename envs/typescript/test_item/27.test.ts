import * as fs from 'fs';
import * as path from 'path';
import { promisify } from 'util';
import { readFile } from 'fs/promises';
import { readdir } from 'fs/promises';
import { join } from 'path';

const readdirAsync = promisify(readdir);
const readFileAsync = promisify(readFile);

async function concatenateJsonArrays(directory: string): Promise<any[]> {
  try {
    const files = await readdirAsync(directory);
    const jsonFiles = files.filter(file => path.extname(file) === '.json');
    const jsonArray = [];

    for (const file of jsonFiles) {
      const filePath = join(directory, file);
      const data = await readFileAsync(filePath, 'utf8');
      const json = JSON.parse(data);
      jsonArray.push(...json);
    }

    return jsonArray;
  } catch (error) {
    console.error('Error reading JSON files:', error);
    throw error;
  }
}
const fs = require('fs');
const path = require('path');
describe('concatenateJsonArrays', () => {
    const testDir = 'test_json';

    beforeAll(() => {
        // Set up test directory and JSON files
        fs.mkdirSync(testDir, { recursive: true });
        fs.writeFileSync(path.join(testDir, 'array1.json'), JSON.stringify([1, 2, 3]));
        fs.writeFileSync(path.join(testDir, 'array2.json'), JSON.stringify(['a', 'b', 'c']));
        fs.writeFileSync(path.join(testDir, 'not_array.json'), JSON.stringify({ key: 'value' }));
        fs.writeFileSync(path.join(testDir, 'empty.json'), JSON.stringify([]));
        fs.writeFileSync(path.join(testDir, 'non_json.txt'), "This is not a JSON file.");
    });

    afterAll(() => {
        // Clean up: Remove created files and directory
        fs.readdirSync(testDir).forEach(file => {
            fs.unlinkSync(path.join(testDir, file));
        });
        fs.rmdirSync(testDir);
    });

    test('concatenate valid JSON arrays', () => {
        const result = concatenateJsonArrays(testDir);
        expect(result).toEqual(expect.arrayContaining([1, 2, 3, 'a', 'b', 'c']));
    });

    test('ignore non-array JSON', () => {
        const result = concatenateJsonArrays(testDir);
        expect(result).not.toContain('key');
    });

    test('ignore non-JSON files', () => {
        const result = concatenateJsonArrays(testDir);
        expect(result).not.toContain("This is not a JSON file.");
    });

    test('handle empty arrays', () => {
        const result = concatenateJsonArrays(testDir);
        expect(result).not.toContain([]);
    });

    test('empty directory', () => {
        const emptyDir = 'empty_test_json';
        fs.mkdirSync(emptyDir, { recursive: true });
        const result = concatenateJsonArrays(emptyDir);
        expect(result).toEqual([]);
        fs.rmdirSync(emptyDir);
    });
});

