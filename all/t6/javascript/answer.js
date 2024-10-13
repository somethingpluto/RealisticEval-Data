const path = require('path');

function simplifyWindowsPath(inputPath) {
    // Split the input path into drive and path components
    const drive = path.parse(inputPath).root;
    const pathWithoutDrive = inputPath.slice(drive.length);

    // Simplify the drive component by replacing ':' with '_'
    const simplifiedDrive = drive.replace(':', '_');

    // Replace backslashes with underscores and strip any trailing underscore
    const simplifiedPath = pathWithoutDrive.replace(/\\/g, '_').replace(/_+$/, '');

    // Concatenate the simplified drive and the remaining path
    const finalPath = simplifiedDrive + simplifiedPath;

    return finalPath;
}