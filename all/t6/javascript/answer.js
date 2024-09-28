const path = require('path');

function simplifyWindowsPath(inputPath) {
    // Extract the drive and the rest of the path
    const drive = path.parse(inputPath).root;
    let pathWithoutDrive = inputPath.substring(drive.length);

    // Simplify the drive (replace colon ':' with underscore '_')
    let simplifiedDrive = drive.replace(':', '_');

    // Replace backslashes '\' with underscores '_' and remove leading and trailing underscores
    let simplifiedPath = pathWithoutDrive.replace(/\\/g, '_').replace(/^_+|_+$/g, '');

    // Concatenate the simplified drive and the rest of the simplified path
    let finalPath = simplifiedDrive + simplifiedPath;

    return finalPath;
}

// Example usage:
console.log(simplifyWindowsPath('D:\\example\\path\\file.txt')); // Output: 'D_example_path_file.txt'