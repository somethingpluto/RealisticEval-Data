const fs = require('fs');
const path = require('path');

/**
 * Renames PNG files in a specified directory by appending a sequence number to each file.
 * The files are sorted alphabetically, and each base name is assigned sequential numbers.
 * For example:
 *   If the directory contains three PNG files such as "image1.png", "image2.png", "image3.png",
 *   after renaming, the PNG files will be "image1001.png", "image2001.png", "image3001.png".
 *
 * @param {string} directory - The path to the directory containing PNG files to be renamed.
 * @returns {void} 
 * @throws {Error} Throws an error if the directory cannot be accessed or if an error occurs during renaming.
 */
function renameFiles(directory) {
    try {
        // Read the directory contents
        const files = fs.readdirSync(directory);

        // Filter out only the PNG files
        const pngFiles = files.filter(file => path.extname(file).toLowerCase() === '.png');

        // Sort the PNG files alphabetically
        pngFiles.sort();

        // Rename each file with a sequence number
        pngFiles.forEach((file, index) => {
            const oldPath = path.join(directory, file);
            const baseName = path.basename(file, '.png');
            const newName = `${baseName}${String(index + 1).padStart(4, '0')}.png`;
            const newPath = path.join(directory, newName);

            // Rename the file
            fs.renameSync(oldPath, newPath);
        });
    } catch (error) {
        throw new Error(`Error renaming files: ${error.message}`);
    }
}
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

