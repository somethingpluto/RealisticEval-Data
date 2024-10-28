import * as fs from 'fs';
import * as path from 'path';
import * as csv from 'csv-parser';

/**
 * Copy files from folderA to folderB excluding those listed in the specified CSV file.
 *
 * @param folderA - Path to the source folder containing all files.
 * @param csvFile - Path to the CSV file containing filenames to exclude.
 * @param folderB - Path to the destination folder.
 * @returns A promise that resolves when the operation is complete.
 */
function extractFilesExcludingCsv(folderA: string, csvFile: string, folderB: string): Promise<void> {
    return new Promise((resolve, reject) => {
        // Ensure folderB exists
        fs.mkdir(folderB, { recursive: true }, (err) => {
            if (err) {
                return reject(new Error(`Unable to create destination folder: ${err.message}`));
            }

            const filenames: Set<string> = new Set();

            // Read the filenames from the CSV file
            fs.createReadStream(csvFile)
                .pipe(csv())
                .on('data', (row) => {
                    // Assuming the filename is in the first column
                    const filename: string = Object.values(row)[0] as string;
                    filenames.add(filename);
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
                                return new Promise<void>((resolveCopy, rejectCopy) => {
                                    fs.copyFile(src, dst, (err) => {
                                        if (err) {
                                            return rejectCopy(new Error(`Error copying file ${file}: ${err.message}`));
                                        }
                                        resolveCopy();
                                    });
                                });
                            }
                        });

                        // Wait for all copy operations to complete
                        Promise.all(copyPromises.filter(Boolean) as Promise<void>[])
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

// Example usage
// extractFilesExcludingCsv('./path/to/source', './path/to/exclude.csv', './path/to/destination')
//     .then(() => console.log('Files copied successfully!'))
//     .catch(err => console.error(err));
