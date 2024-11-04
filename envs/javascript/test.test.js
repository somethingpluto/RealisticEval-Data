const fs = require('fs');
const path = require('path');

function emptyDirectory(directoryPath) {
    /**
     * Empties all files and subdirectories in the specified directory.
     * @param {string} directoryPath - The path to the directory whose contents are to be emptied.
     * @returns {Promise<void>} A promise that resolves when the directory is emptied or rejects with an error.
     */
    
    return new Promise((resolve, reject) => {
        if (!fs.existsSync(directoryPath)) {
            return reject(new Error(`The specified path ${directoryPath} does not exist.`));
        }

        if (!fs.lstatSync(directoryPath).isDirectory()) {
            return reject(new Error(`${directoryPath} is not a directory.`));
        }

        fs.readdir(directoryPath, (err, files) => {
            if (err) {
                return reject(err);
            }

            const promises = files.map(file => {
                const filePath = path.join(directoryPath, file);

                return new Promise((resolve, reject) => {
                    fs.stat(filePath, (err, stats) => {
                        if (err) {
                            return reject(err);
                        }

                        if (stats.isDirectory()) {
                            fs.promises.rmdir(filePath, { recursive: true })
                                .then(resolve)
                                .catch(reject);
                        } else {
                            fs.unlink(filePath)
                                .then(resolve)
                                .catch(reject);
                        }
                    });
                });
            });

            Promise.all(promises)
                .then(() => resolve())
                .catch(reject);
        });
    });
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
