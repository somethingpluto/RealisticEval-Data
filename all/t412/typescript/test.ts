import * as fs from 'fs';
import * as path from 'path';
import { tmpdir } from 'os';

describe('TestFormatText', () => {
    beforeEach(() => {
        // Before each test, clean up any temporary files
        jest.resetModules();
    });

    afterEach(() => {
        // After each test, clean up any temporary files
        const cleanup = (filePath: string) => {
            if (fs.existsSync(filePath)) {
                fs.unlinkSync(filePath);
            }
        };

        cleanup(tmpInputFilePath);
        cleanup(tmpOutputFilePath);
    });

    let tmpInputFilePath: string;
    let tmpOutputFilePath: string;

    const createTempFile = (content: string): string => {
        const tempFilePath = path.join(tmpdir(), `temp-${Date.now()}.txt`);
        fs.writeFileSync(tempFilePath, content);
        return tempFilePath;
    };

    describe('test_basic_text', () => {
        it('should format basic text correctly', () => {
            const inputText = "This is line one.\nThis is line two.\nThis is line three.";
            const expectedOutput = "This is line one. This is line two. This is line three.";

            tmpInputFilePath = createTempFile(inputText);
            tmpOutputFilePath = createTempFile('');

            formatText(tmpInputFilePath, tmpOutputFilePath);

            return new Promise<void>((resolve, reject) => {
                fs.readFile(tmpOutputFilePath, 'utf8', (err, data) => {
                    if (err) {
                        reject(err);
                    } else {
                        expect(data.trim()).toBe(expectedOutput);
                        resolve();
                    }
                });
            });
        });
    });

    describe('test_single_line', () => {
        it('should format a single line correctly', () => {
            const inputText = "This is a single line.";
            const expectedOutput = "This is a single line.";

            tmpInputFilePath = createTempFile(inputText);
            tmpOutputFilePath = createTempFile('');

            formatText(tmpInputFilePath, tmpOutputFilePath);

            return new Promise<void>((resolve, reject) => {
                fs.readFile(tmpOutputFilePath, 'utf8', (err, data) => {
                    if (err) {
                        reject(err);
                    } else {
                        expect(data.trim()).toBe(expectedOutput);
                        resolve();
                    }
                });
            });
        });
    });

    describe('test_empty_file', () => {
        it('should handle an empty file correctly', () => {
            const inputText = "";
            const expectedOutput = "";

            tmpInputFilePath = createTempFile(inputText);
            tmpOutputFilePath = createTempFile('');

            formatText(tmpInputFilePath, tmpOutputFilePath);

            return new Promise<void>((resolve, reject) => {
                fs.readFile(tmpOutputFilePath, 'utf8', (err, data) => {
                    if (err) {
                        reject(err);
                    } else {
                        expect(data.trim()).toBe(expectedOutput);
                        resolve();
                    }
                });
            });
        });
    });

    describe('test_file_with_no_newlines', () => {
        it('should handle a file with no newlines correctly', () => {
            const inputText = "This is a continuous line without breaks.";
            const expectedOutput = "This is a continuous line without breaks.";

            tmpInputFilePath = createTempFile(inputText);
            tmpOutputFilePath = createTempFile('');

            formatText(tmpInputFilePath, tmpOutputFilePath);

            return new Promise<void>((resolve, reject) => {
                fs.readFile(tmpOutputFilePath, 'utf8', (err, data) => {
                    if (err) {
                        reject(err);
                    } else {
                        expect(data.trim()).toBe(expectedOutput);
                        resolve();
                    }
                });
            });
        });
    });
});