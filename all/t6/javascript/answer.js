const path = require('path');

function simplifyWindowsPath(inputPath) {
    // Use path.parse to get the drive and path information
    const parsedPath = path.parse(inputPath);
    const drive = parsedPath.root; // This gives the drive letter (e.g., 'D:\\')
    const pathWithoutDrive = parsedPath.dir; // This gives the directory without the drive

    // Simplify the drive
    const simplifiedDrive = drive.replace(':', '').replace('\\', '_'); // Replace ':' and the first '\' with '_'

    // Replace backslashes with underscores and strip any trailing underscores
    const simplifiedPath = pathWithoutDrive.replace(/\\/g, '_').replace(/_$/, ''); // Replace backslashes with underscores

    // Concatenate the simplified drive and the remaining path
    const finalPath = `${simplifiedDrive}${simplifiedPath}`;

    return finalPath;
}