import * as fs from 'fs';
import * as path from 'path';
import * as os from 'os';
import * as glob from 'glob';

function renameFiles(directory: string): void {
    const dirPath = path.resolve(directory);

    if (!fs.existsSync(dirPath) || !fs.lstatSync(dirPath).isDirectory()) {
        throw new Error(`The directory '${directory}' does not exist or is not a directory.`);
    }

    // Get list of PNG files in the directory
    const pngFilesPattern = path.join(dirPath, '*.png');
    const pngFiles = glob.sync(pngFilesPattern);

    // Sort files alphabetically by their names
    pngFiles.sort();

    // Print the sorted list of files (for debugging)
    console.log("Sorted files:");
    pngFiles.forEach(file => {
        console.log(path.basename(file));
    });

    // Rename files with sequence numbers
    let prevBaseName: string | null = null;
    let count = 1;

    pngFiles.forEach(file => {
        // Extract base name without postfix and number
        const baseName = file.replace(/(\d{3})(-\d)?(?=\.png$)/, '');

        if (baseName !== prevBaseName) {
            count = 1;
        }

        const newFileName = `${baseName}${count.toString().padStart(3, '0')}.png`;
        const newFilePath = path.join(dirPath, newFileName);
        fs.renameSync(file, newFilePath);
        console.log(`Renaming ${path.basename(file)} to ${newFileName}`);

        prevBaseName = baseName;
        count++;
    });
}
