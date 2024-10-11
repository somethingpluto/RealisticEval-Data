describe('emptyDirectory', () => {
    let tempDir;

    beforeEach(() => {
        // Create a temporary directory for testing
        tempDir = fs.mkdtempSync(path.join(__dirname, 'test-dir-'));
        fs.mkdirSync(path.join(tempDir, 'subdir'));
        fs.writeFileSync(path.join(tempDir, 'file.txt'), 'Some content');
    });

    afterEach(() => {
        // Clean up the temporary directory after each test
        emptyDirectory(tempDir);
        fs.rmdirSync(tempDir);
    });

    it('should empty a directory with files and subdirectories', () => {
        expect(fs.readdirSync(tempDir)).toEqual(['subdir', 'file.txt']);
        emptyDirectory(tempDir);
        expect(fs.readdirSync(tempDir)).toEqual([]);
    });

    it('should throw an error if the path does not exist', () => {
        expect(() => emptyDirectory('/nonexistent/path')).toThrow(/does not exist/);
    });

    it('should throw an error if the path is not a directory', () => {
        const filePath = path.join(tempDir, 'file.txt');
        fs.writeFileSync(filePath, 'Some content');
        expect(() => emptyDirectory(filePath)).toThrow(/is not a directory/);
    });
});