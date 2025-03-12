const fs = require('fs').promises;
const path = require('path');

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
    try {
        // Check if the directory exists and is a directory
        const stats = await fs.stat(directoryPath);
        if (!stats.isDirectory()) {
            throw new Error(`The specified path is not a directory: ${directoryPath}`);
        }

        // Read the directory contents
        const items = await fs.readdir(directoryPath);

        // Iterate over each item in the directory
        for (const item of items) {
            const itemPath = path.join(directoryPath, item);
            const itemStats = await fs.stat(itemPath);

            if (itemStats.isDirectory()) {
                // Recursively empty the subdirectory
                await emptyDirectory(itemPath);
                // Remove the now-empty subdirectory
                await fs.rmdir(itemPath);
            } else {
                // Remove the file
                await fs.unlink(itemPath);
            }
        }
    } catch (error) {
        if (error.code === 'ENOENT') {
            throw new Error(`The specified path does not exist: ${directoryPath}`);
        }
        throw error;
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
