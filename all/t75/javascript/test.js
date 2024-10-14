describe('TestRenameFiles', () => {
    let testDir;

    beforeAll(() => {
        testDir = mkdtempSync(path.join(os.tmpdir(), 'test-rename-files-'));
    });

    afterAll(() => {
        rmSync(testDir, { recursive: true });
    });

    beforeEach(() => {
        // Ensure the test directory is clean before each test
        fs.readdirSync(testDir).forEach(file => {
            fs.unlinkSync(path.join(testDir, file));
        });
    });

    function createPngFiles(filenames) {
        filenames.forEach(filename => {
            const filePath = path.join(testDir, filename);
            fs.writeFileSync(filePath, '');
        });
    }

    it('should rename files in a basic scenario with simple filenames', () => {
        const filenames = ["image1.png", "image2.png", "image3.png"];
        createPngFiles(filenames);

        renameFiles(testDir);

        const expectedFiles = ['image1001.png', 'image2001.png', 'image3001.png'];
        const resultFiles = readdirSync(testDir).sort();
        expect(resultFiles).toEqual(expectedFiles);
    });

    it('should reset the counter for different base names', () => {
        const filenames = ["image1.png", "picture1.png", "image2.png", "picture2.png"];
        createPngFiles(filenames);

        renameFiles(testDir);

        const expectedFiles = ['image1001.png', 'image2001.png', 'picture1001.png', 'picture2001.png'];
        const resultFiles = readdirSync(testDir).sort();
        expect(resultFiles).toEqual(expectedFiles);
    });

    it('should handle directories with no PNG files', () => {
        const filenames = ["file1.txt", "file2.jpg"];
        createPngFiles(filenames);

        renameFiles(testDir);

        const expectedFiles = filenames;
        const resultFiles = readdirSync(testDir).sort();
        expect(resultFiles).toEqual(expectedFiles);
    });

    it('should handle an empty directory', () => {
        renameFiles(testDir);

        const expectedFiles = [];
        const resultFiles = readdirSync(testDir);
        expect(resultFiles).toEqual(expectedFiles);
    });

    it('should rename files that already have numbers in their names', () => {
        const filenames = ["file001.png", "file002.png", "file003.png"];
        createPngFiles(filenames);

        renameFiles(testDir);

        const expectedFiles = ['file001001.png', 'file002001.png', 'file003001.png'];
        const resultFiles = readdirSync(testDir).sort();
        expect(resultFiles).toEqual(expectedFiles);
    });
});
