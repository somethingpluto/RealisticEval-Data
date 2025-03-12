import { readFile } from 'fs/promises';
import { createReadStream } from 'fs';
import { createInterface } from 'readline';

async function readFileToByteArray(filePath: string): Promise<Uint8Array> {
  return new Promise((resolve, reject) => {
    const stream = createReadStream(filePath);
    const chunks: Buffer[] = [];

    stream.on('data', (chunk: Buffer) => {
      chunks.push(chunk);
    });

    stream.on('end', () => {
      resolve(Buffer.concat(chunks)).buffer as Uint8Array;
    });

    stream.on('error', (err) => {
      reject(err);
    });
  });
}
import * as fs from 'fs';

describe('File Operations', () => {
    const testFile = 'testFile.txt';

    beforeEach(() => {
        fs.writeFileSync(testFile, Buffer.from('Test content'));
    });

    afterEach(() => {
        if (fs.existsSync(testFile)) {
            fs.unlinkSync(testFile);
        }
    });

    test('read file with content', () => {
        const content = readFileToByteArray(testFile);
        expect(content).toEqual(Buffer.from('Test content'));
    });

    test('read empty file', () => {
        const emptyFile = 'emptyFile.txt';
        fs.writeFileSync(emptyFile, '');
        const content = readFileToByteArray(emptyFile);
        expect(content.length).toBe(0);
        fs.unlinkSync(emptyFile);
    });

    test('read non-existent file', () => {
        const nonExistentFilePath = 'nonExistentFile.txt';
        expect(() => readFileToByteArray(nonExistentFilePath)).toThrow();
    });

    test('read file with special characters', () => {
        const specialContent = 'Special content: !@#$%^&*()_+';
        fs.writeFileSync(testFile, Buffer.from(specialContent));
        const content = readFileToByteArray(testFile);
        expect(content).toEqual(Buffer.from(specialContent));
    });

    test('read large file', () => {
        const largeContent = Buffer.from(Array.from({ length: 256 }, (_, i) => i).flatMap(i => Array(10).fill(i)));
        fs.writeFileSync(testFile, largeContent);
        const content = readFileToByteArray(testFile);
        expect(content).toEqual(largeContent);
    });
});
