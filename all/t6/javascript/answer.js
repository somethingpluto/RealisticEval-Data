function simplifyWindowsPath(path) {
    const driveMatch = path.match(/^([A-Z]):/i);
    let simplifiedDrive = '';
    let simplifiedPath = path;

    if (driveMatch) {
        simplifiedDrive = driveMatch[1] + '_'; // Replace the colon with an underscore (e.g., "C:" becomes "C_")
        simplifiedPath = path.slice(driveMatch[0].length); // Remove the drive part from the path
    }

    // Only replace the backslashes if the path is not empty
    simplifiedPath = simplifiedPath.replace(/\\/g, '_').replace(/^_/, ''); // Remove leading underscore if path starts with '\'
    
    return simplifiedDrive + simplifiedPath;
}
