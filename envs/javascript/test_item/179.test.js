const fs = require('fs');
const path = require('path');

/**
 * Copies all files and subdirectories from the source directory to the target directory.
 *
 * @param {string} sourceDir - The source directory from which files and subdirectories will be copied.
 * @param {string} targetDir - The target directory to which files and subdirectories will be copied.
 * @returns {void}
 */
function copyDirectory(sourceDir, targetDir) {
  // Ensure the target directory exists
  if (!fs.existsSync(targetDir)){
    fs.mkdirSync(targetDir, { recursive: true });
  }

  // Read the contents of the source directory
  const files = fs.readdirSync(sourceDir);

  // Iterate over each file and directory
  files.forEach(file => {
    const sourcePath = path.join(sourceDir, file);
    const targetPath = path.join(targetDir, file);

    // Check if the item is a file or a directory
    const stat = fs.lstatSync(sourcePath);

    if (stat.isDirectory()) {
      // If it's a directory, recursively copy it
      copyDirectory(sourcePath, targetPath);
    } else {
      // If it's a file, copy it
      fs.copyFileSync(sourcePath, targetPath);
    }
  });
}
const fs = require('fs');
const path = require('path');
describe('Directory Operations', () => {
    const sourceDir = 'testSourceDir';
    const targetDir = 'testTargetDir';

    beforeEach(() => {
        // Setup: Create source and target directories
        fs.mkdirSync(sourceDir, { recursive: true });
        fs.mkdirSync(targetDir, { recursive: true });
    });

    afterEach(() => {
        // Teardown: Delete source and target directories
        deleteDirectory(sourceDir);
        deleteDirectory(targetDir);
    });

    function deleteDirectory(dirPath) {
        if (fs.existsSync(dirPath)) {
            fs.rmdirSync(dirPath, { recursive: true });
        }
    }

    test('copy empty directory', () => {
        // Simulating copyDirectory functionality
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
        }).toThrow('Source directory does not exist.');
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
        // Create a source file with some content
        const testFile = path.join(sourceDir, 'testFile.txt');
        fs.writeFileSync(testFile, 'Source content');

        // Create a target file with different content
        const targetFile = path.join(targetDir, 'testFile.txt');
        fs.writeFileSync(targetFile, 'Target content');

        // Copy the directory, which should overwrite the target file
        copyDirectory(sourceDir, targetDir);

        const copiedFile = path.join(targetDir, 'testFile.txt');
        expect(fs.existsSync(copiedFile)).toBe(true);

        // Check that the content of the file is now the same as the source file
        const copiedContent = fs.readFileSync(copiedFile, 'utf-8');
        expect(copiedContent).toBe('Source content');
    });
});
