describe('findMarkdownFiles', () => {
    const testDir = path.join(__dirname, 'test_dir');

    beforeAll(() => {
        // Create a temporary test directory structure
        fs.mkdirSync(testDir, { recursive: true });
        fs.mkdirSync(path.join(testDir, 'subdir1'), { recursive: true });
        fs.mkdirSync(path.join(testDir, 'subdir2'), { recursive: true });

        // Create Markdown files
        fs.writeFileSync(path.join(testDir, 'file1.md'), 'Markdown content 1');
        fs.writeFileSync(path.join(testDir, 'subdir1', 'file2.md'), 'Markdown content 2');
        fs.writeFileSync(path.join(testDir, 'subdir2', 'file3.md'), 'Markdown content 3');

        // Create non-Markdown files
        fs.writeFileSync(path.join(testDir, 'file4.txt'), 'Some text content');
        fs.writeFileSync(path.join(testDir, 'subdir1', 'file5.txt'), 'Some more text content');
        fs.writeFileSync(path.join(testDir, 'subdir2', 'file6.doc'), 'Document content');
    });

    afterAll(() => {
        // Clean up the test directory
        fs.rmdirSync(testDir, { recursive: true });
    });

    test('should find Markdown files in the root directory', () => {
        const result = findMarkdownFiles(testDir);
        expect(result).toEqual(
            expect.arrayContaining([
                path.join(testDir, 'file1.md'),
                path.join(testDir, 'subdir1', 'file2.md'),
                path.join(testDir, 'subdir2', 'file3.md'),
            ])
        );
    });

    test('should not return non-Markdown files', () => {
        const result = findMarkdownFiles(testDir);
        expect(result).not.toEqual(
            expect.arrayContaining([
                path.join(testDir, 'file4.txt'),
                path.join(testDir, 'subdir1', 'file5.txt'),
                path.join(testDir, 'subdir2', 'file6.doc'),
            ])
        );
    });

    test('should return an empty array when no Markdown files exist', () => {
        const emptyDir = path.join(__dirname, 'empty_dir');
        fs.mkdirSync(emptyDir, { recursive: true });
        const result = findMarkdownFiles(emptyDir);
        expect(result).toEqual([]);
        fs.rmdirSync(emptyDir);
    });

    test('should handle deeply nested directories', () => {
        fs.mkdirSync(path.join(testDir, 'subdir1', 'subsubdir'), { recursive: true });
        fs.writeFileSync(path.join(testDir, 'subdir1', 'subsubdir', 'file7.md'), 'Markdown content 4');

        const result = findMarkdownFiles(testDir);
        expect(result).toEqual(
            expect.arrayContaining([
                path.join(testDir, 'file1.md'),
                path.join(testDir, 'subdir1', 'file2.md'),
                path.join(testDir, 'subdir2', 'file3.md'),
                path.join(testDir, 'subdir1', 'subsubdir', 'file7.md'),
            ])
        );
    });
});