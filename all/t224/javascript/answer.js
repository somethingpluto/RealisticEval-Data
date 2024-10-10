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