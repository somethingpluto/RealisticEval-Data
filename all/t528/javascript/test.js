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
        expect(result).toEqual(['dir/file1.md']);
    });

    test('should return an array with multiple Markdown files in the same directory', () => {
        fs.readdirSync.mockReturnValue(['file1.md', 'file2.md']);
        fs.statSync.mockImplementation(file => ({
            isDirectory: () => false,
        }));

        const result = findMarkdownFiles('dir');
        expect(result).toEqual(['dir/file1.md', 'dir/file2.md']);
    });

    test('should handle nested directories and return all Markdown files', () => {
        fs.readdirSync.mockImplementation(dir => {
            if (dir === 'dir') return ['subdir', 'file1.md'];
            if (dir === 'dir/subdir') return ['file2.md'];
            return [];
        });

        fs.statSync.mockImplementation(file => {
            if (file === path.join('dir', 'subdir')) {
                return {isDirectory: () => true};
            }
            return {isDirectory: () => false};
        });

        const result = findMarkdownFiles('dir');
        expect(result).toEqual([
            'dir/file1.md',
            'dir/subdir/file2.md',
        ]);
    });

    test('should return Markdown files while ignoring non-Markdown files', () => {
        fs.readdirSync.mockReturnValue(['file1.txt', 'file2.md', 'file3.doc']);
        fs.statSync.mockImplementation(file => ({
            isDirectory: () => false,
        }));

        const result = findMarkdownFiles('dir');
        expect(result).toEqual(['dir/file2.md']);
    });

    test('should recursively search through multiple levels of directories', () => {
        fs.readdirSync.mockImplementation(dir => {
            if (dir === 'dir') return ['file1.md', 'subdir1'];
            if (dir === 'dir/subdir1') return ['file2.md', 'subdir2'];
            if (dir === 'dir/subdir1/subdir2') return ['file3.md'];
            return [];
        });

        fs.statSync.mockImplementation(file => {
            if (file === path.join('dir', 'subdir1')) {
                return {isDirectory: () => true};
            }
            if (file === path.join('dir', 'subdir1', 'subdir2')) {
                return {isDirectory: () => true};
            }
            return {isDirectory: () => false};
        });

        const result = findMarkdownFiles('dir');
        expect(result).toEqual([
            'dir/file1.md',
            'dir/subdir1/file2.md',
            'dir/subdir1/subdir2/file3.md',
        ]);
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