const fs = require('fs');
const path = require('path');

/**
 * Searches for Markdown files in the specified directory and returns the path of the files as an array
 *
 * @param {string} dir - The directory path to search in.
 * @returns {string[]} - An array of paths to Markdown files.
 */
function findMarkdownFiles(dir) {
    let markdownFiles = [];

    function traverseDirectory(currentDir) {
        const files = fs.readdirSync(currentDir);

        files.forEach(file => {
            const filePath = path.join(currentDir, file);
            const stat = fs.statSync(filePath);

            if (stat.isDirectory()) {
                traverseDirectory(filePath);
            } else if (stat.isFile() && path.extname(file).toLowerCase() === '.md') {
                markdownFiles.push(filePath);
            }
        });
    }

    traverseDirectory(dir);
    return markdownFiles;
}
const fs = require('fs');
const path = require('path');

jest.mock('fs');

describe('findMarkdownFiles', () => {
    beforeEach(() => {
        jest.clearAllMocks();
    });

    test('should return an empty array for an empty directory', () => {
        fs.readdirSync.mockReturnValue([]);
        fs.statSync.mockImplementation(() => ({isDirectory: () => false}));

        const result = findMarkdownFiles('emptyDir');
        expect(result).toEqual([]);
    });

    test('should return an array with one Markdown file', () => {
        fs.readdirSync.mockReturnValue(['file1.md']);
        fs.statSync.mockImplementation(file => ({
            isDirectory: () => false,
        }));

        const result = findMarkdownFiles('dir');
        expect(result).toEqual(['dir\\file1.md']);
    });

    test('should return an array with multiple Markdown files in the same directory', () => {
        fs.readdirSync.mockReturnValue(['file1.md', 'file2.md']);
        fs.statSync.mockImplementation(file => ({
            isDirectory: () => false,
        }));

        const result = findMarkdownFiles('dir');
        expect(result).toEqual(['dir\\file1.md', 'dir\\file2.md']);
    });


    test('should return Markdown files while ignoring non-Markdown files', () => {
        fs.readdirSync.mockReturnValue(['file1.txt', 'file2.md', 'file3.doc']);
        fs.statSync.mockImplementation(file => ({
            isDirectory: () => false,
        }));

        const result = findMarkdownFiles('dir');
        expect(result).toEqual(['dir\\file2.md']);
    });


    test('should handle a directory with only non-Markdown files', () => {
        fs.readdirSync.mockReturnValue(['file1.txt', 'file2.doc']);
        fs.statSync.mockImplementation(file => ({
            isDirectory: () => false,
        }));

        const result = findMarkdownFiles('dir');
        expect(result).toEqual([]);
    });
});

