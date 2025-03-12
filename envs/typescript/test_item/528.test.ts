import { readdirSync, statSync, join } from 'fs';
import { resolve } from 'path';

function findMarkdownFiles(dir: string): string[] {
  const markdownFiles: string[] = [];
  const entries = readdirSync(dir);

  entries.forEach((entry) => {
    const fullPath = join(dir, entry);
    const stat = statSync(fullPath);

    if (stat.isDirectory()) {
      markdownFiles.push(...findMarkdownFiles(fullPath));
    } else if (entry.endsWith('.md')) {
      markdownFiles.push(fullPath);
    }
  });

  return markdownFiles;
}
import * as fs from 'fs';

jest.mock('fs');

describe('findMarkdownFiles', () => {
    beforeEach(() => {
        jest.clearAllMocks();
    });

    test('should return an empty array for an empty directory', () => {
        (fs.readdirSync as jest.Mock).mockReturnValue([]);
        (fs.statSync as jest.Mock).mockImplementation(() => ({ isDirectory: () => false }));

        const result = findMarkdownFiles('emptyDir');
        expect(result).toEqual([]);
    });

    test('should return an array with one Markdown file', () => {
        (fs.readdirSync as jest.Mock).mockReturnValue(['file1.md']);
        (fs.statSync as jest.Mock).mockImplementation(() => ({ isDirectory: () => false }));

        const result = findMarkdownFiles('dir');
        expect(result).toEqual(['dir\\file1.md']);
    });

    test('should return an array with multiple Markdown files in the same directory', () => {
        (fs.readdirSync as jest.Mock).mockReturnValue(['file1.md', 'file2.md']);
        (fs.statSync as jest.Mock).mockImplementation(() => ({ isDirectory: () => false }));

        const result = findMarkdownFiles('dir');
        expect(result).toEqual(['dir\\file1.md', 'dir\\file2.md']);
    });

    test('should return Markdown files while ignoring non-Markdown files', () => {
        (fs.readdirSync as jest.Mock).mockReturnValue(['file1.txt', 'file2.md', 'file3.doc']);
        (fs.statSync as jest.Mock).mockImplementation(() => ({ isDirectory: () => false }));

        const result = findMarkdownFiles('dir');
        expect(result).toEqual(['dir\\file2.md']);
    });

    test('should handle a directory with only non-Markdown files', () => {
        (fs.readdirSync as jest.Mock).mockReturnValue(['file1.txt', 'file2.doc']);
        (fs.statSync as jest.Mock).mockImplementation(() => ({ isDirectory: () => false }));

        const result = findMarkdownFiles('dir');
        expect(result).toEqual([]);
    });
});
