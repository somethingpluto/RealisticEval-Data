import fs from 'fs';
import path from 'path';
describe('TestDirectoryOperations', () => {
    const sourceDir = 'testSourceDir';
    const targetDir = 'testTargetDir';

    beforeAll(() => {
        fs.mkdirSync(sourceDir, { recursive: true });
        fs.mkdirSync(targetDir, { recursive: true });
    });

    afterAll(() => {
        deleteDirectory(sourceDir);
        deleteDirectory(targetDir);
    });

    const deleteDirectory = (dirPath: string): void => {
        if (fs.existsSync(dirPath)) {
            fs.rmdirSync(dirPath, { recursive: true });
        }
    };

    test('copy empty directory', () => {
        copyDirectory(sourceDir, targetDir);
        expect(fs.existsSync(targetDir)).toBe(true);
        expect(fs.statSync(targetDir).isDirectory()).toBe(true);
        expect(fs.readdirSync(targetDir).length).toBe(0);
    });

    test('copy directory with files', () => {
        const testFile = path.join(sourceDir, 'testFile.txt');
        fs.writeFileSync(testFile, 'Sample content');

        copyDirectory(sourceDir, targetDir);
        
        const copiedFile = path.join(targetDir, 'testFile.txt');
        expect(fs.existsSync(copiedFile)).toBe(true);
        expect(fs.statSync(testFile).size).toBe(fs.statSync(copiedFile).size);
    });

    test('non-existent source directory', () => {
        const nonExistentDir = 'nonExistentDir';
        expect(() => {
            copyDirectory(nonExistentDir, targetDir);
        }).toThrowError(new Error('Source directory does not exist.'));
    });

    test('copy directory with subdirectories', () => {
        const subDir = path.join(sourceDir, 'subDir');
        fs.mkdirSync(subDir, { recursive: true });
        const testFile = path.join(subDir, 'testFile.txt');
        fs.writeFileSync(testFile, 'Sample content in subdirectory');

        copyDirectory(sourceDir, targetDir);

        const copiedSubDir = path.join(targetDir, 'subDir');
        const copiedFile = path.join(copiedSubDir, 'testFile.txt');

        expect(fs.existsSync(copiedSubDir)).toBe(true);
        expect(fs.existsSync(copiedFile)).toBe(true);
    });

    test('overwrite file in target directory', () => {
        const testFile = path.join(sourceDir, 'testFile.txt');
        fs.writeFileSync(testFile, 'Source content');

        const targetFile = path.join(targetDir, 'testFile.txt');
        fs.writeFileSync(targetFile, 'Target content');

        copyDirectory(sourceDir, targetDir);

        const copiedFile = path.join(targetDir, 'testFile.txt');
        expect(fs.existsSync(copiedFile)).toBe(true);

        const copiedContent = fs.readFileSync(copiedFile, 'utf-8');
        expect(copiedContent).toBe('Source content');
    });
});