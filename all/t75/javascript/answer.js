const fs = require('fs');
const path = require('path');
const { readdirSync, renameSync } = fs;
const { promisify } = require('util');
const { statSync } = fs;

const readdir = promisify(readdirSync);
const rename = promisify(renameSync);

async function renameFiles(directory) {
    /**
     * Renames PNG files in a specified directory by appending a sequence number to each file.
     * The files are sorted alphabetically, and each base name is assigned sequential numbers.
     *
     * @param {string} directory - The path to the directory containing PNG files to be renamed.
     */

    // Convert directory to Path object for easier handling
    const dirPath = path.resolve(directory);

    if (!statSync(dirPath).isDirectory()) {
        throw new Error(`The directory '${directory}' does not exist or is not a directory.`);
    }

    // Get list of PNG files in the directory
    const pngFiles = await readdir(dirPath).then(files =>
        files.filter(file => statSync(path.join(dirPath, file)).isFile() && path.extname(file).toLowerCase() === '.png')
    );

    // Sort files alphabetically by their names
    pngFiles.sort();

    // Print the sorted list of files (for debugging)
    console.log("Sorted files:");
    pngFiles.forEach(file => console.log(file));

    // Rename files with sequence numbers
    let prevBaseName = null;
    let count = 1;

    for (const file of pngFiles) {
        // Extract base name without postfix and number
        const baseName = file.replace(/(\d{3})(-\d)?(?=\.png$)/, '');

        if (baseName !== prevBaseName) {
            count = 1;
        }

        const newFilename = `${baseName}${count.toString().padStart(3, '0')}.png`;
        const oldFilePath = path.join(dirPath, file);
        const newFilePath = path.join(dirPath, newFilename);

        await rename(oldFilePath, newFilePath);
        console.log(`Renaming ${file} to ${newFilename}`);

        prevBaseName = baseName;
        count += 1;
    }
}
