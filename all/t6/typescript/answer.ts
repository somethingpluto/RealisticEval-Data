function simplifyWindowsPath(path: string): string {
    // Function to split the drive and the rest of the path
    function splitDrive(path: string): { drive: string, pathWithoutDrive: string } {
        const match = /^[A-Za-z]:/.exec(path);
        if (match) {
            const drive = match[0];
            const pathWithoutDrive = path.slice(drive.length);
            return { drive, pathWithoutDrive };
        }
        return { drive: '', pathWithoutDrive: path };
    }

    // Split the drive and the rest of the path
    const { drive, pathWithoutDrive } = splitDrive(path);
    const simplifiedDrive = drive.replace(':', '_');

    // Replace backslashes with underscores and strip any trailing backslash
    const simplifiedPath = pathWithoutDrive.replace(/\\/g, '_').replace(/^_|_$/g, '');

    // Concatenate the simplified drive and the remaining path
    const finalPath = simplifiedDrive + simplifiedPath;

    return finalPath;
}

// Example Usage
const originalPath = "D:\\some\\path\\to\\file\\";
const simplifiedPath = simplifyWindowsPath(originalPath);
console.log(simplifiedPath);