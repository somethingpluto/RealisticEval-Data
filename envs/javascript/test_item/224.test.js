/**
 * Empties all files and subdirectories in the specified directory.
 * 
 * @param {string} directoryPath - Path to the directory whose contents are to be emptied.
 * 
 * @returns {Promise<void>} - A promise that resolves when the operation is complete.
 * 
 * @throws {Error} - If the specified path does not exist or is not a directory.
 */
async function emptyDirectory(directoryPath) {
    const fs = require('fs').promises;
    const path = require('path');

    try {
        const entries = await fs.readdir(directoryPath, { withFileTypes: true });

        for (const entry of entries) {
            const fullPath = path.join(directoryPath, entry.name);
            if (entry.isDirectory()) {
                await emptyDirectory(fullPath);
                await fs.rmdir(fullPath);
            } else {
                await fs.unlink(fullPath);
            }
        }
    } catch (error) {
        if (error.code === 'ENOENT') {
            throw new Error('The specified path does not exist.');
        } else if (error.code !== 'ENOTDIR') {
            throw error;
        }
    }
}
const fs = require('fs');
const path = require('path');
const { rm, unlink } = require('fs').promises;
const { mkdtemp, rmdir } = require('fs').promises;

describe('TestEmptyDirectory', () => {
    let testDir;

    beforeAll(async () => {
        // Set up a temporary directory with some files and directories
        testDir = await mkdtemp(path.join(os.tmpdir(), 'test-'));
        // Create some files and directories
        await fs.promises.mkdir(path.join(testDir, 'subdir'));
        await fs.promises.writeFile(path.join(testDir, 'file1.txt'), 'Hello');
        await fs.promises.writeFile(path.join(testDir, 'subdir', 'file2.txt'), 'World');
    });

    afterAll(async () => {
        // Remove the temporary directory after all tests
        await rmdir(testDir, { recursive: true });
    });

    it('should empty the directory successfully', async () => {
        // Test that the directory is emptied successfully
        await emptyDirectory(testDir);
        expect(await fs.promises.readdir(testDir)).toEqual([]);
    });

    it('should empty a directory that includes subdirectories', async () => {
        // Test emptying a directory that includes subdirectories
        await emptyDirectory(testDir);
        expect(await fs.promises.readdir(testDir)).toEqual([]);
    });

    it('should handle an already empty directory', async () => {
        // Test emptying a directory that is already empty
        await emptyDirectory(testDir);  // First emptying
        await emptyDirectory(testDir);  // Empty again
        expect(await fs.promises.readdir(testDir)).toEqual([]);
    });
});
