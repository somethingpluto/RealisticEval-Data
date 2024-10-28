const fs = require('fs');
const path = require('path');
const csv = require('csv-parser');

/**
 * Copy files from folderA to folderB excluding those listed in the specified CSV file.
 *
 * @param {string} folderA - Path to the source folder containing all files.
 * @param {string} csvFile - Path to the CSV file containing filenames to exclude.
 * @param {string} folderB - Path to the destination folder.
 * @returns {Promise<void>} A promise that resolves when the operation is complete.
 */
function extractFilesExcludingCsv(folderA, csvFile, folderB) {
    return new Promise((resolve, reject) => {
        // Ensure folderB exists
        fs.mkdir(folderB, { recursive: true }, (err) => {
            if (err) {
                return reject(new Error(`Unable to create destination folder: ${err.message}`));
            }

            const filenames = new Set();

            // Read the filenames from the CSV file
            fs.createReadStream(csvFile)
                .pipe(csv())
                .on('data', (row) => {
                    // Assuming the filename is in the first column
                    filenames.add(row[Object.keys(row)[0]]);
                })
                .on('end', () => {
                    // Copy all files from folderA to folderB that are not in the CSV file
                    fs.readdir(folderA, (err, files) => {
                        if (err) {
                            return reject(new Error(`Unable to read source folder: ${err.message}`));
                        }

                        const copyPromises = files.map((file) => {
                            if (!filenames.has(file)) {
                                const src = path.join(folderA, file);
                                const dst = path.join(folderB, file);
                                return new Promise((resolve, reject) => {
                                    fs.copyFile(src, dst, (err) => {
                                        if (err) {
                                            return reject(new Error(`Error copying file ${file}: ${err.message}`));
                                        }
                                        resolve();
                                    });
                                });
                            }
                        });

                        // Wait for all copy operations to complete
                        Promise.all(copyPromises.filter(Boolean))
                            .then(resolve)
                            .catch(reject);
                    });
                })
                .on('error', (err) => {
                    reject(new Error(`Error reading CSV file: ${err.message}`));
                });
        });
    });
}