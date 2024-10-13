const path = require('path')
function simplifyWindowsPath(inputPath: string): string {
    // Replace the drive letter and colon, e.g., 'D:' with 'D_'
    const [drive, pathWithoutDrive] = path.parse(inputPath);
    const simplifiedDrive = drive.replace(':', '') + '_';
  
    // Replace backslashes with underscores and strip any trailing backslash
    const simplifiedPath = pathWithoutDrive.replace(/\\/g, '_').replace(/_+$/, '');
  
    // Concatenate the simplified drive and the remaining path
    const finalPath = simplifiedDrive + simplifiedPath;
  
    return finalPath;
  }