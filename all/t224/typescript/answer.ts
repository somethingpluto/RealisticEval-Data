function emptyDirectory(directoryPath: string): void | Error {
    /**
     * Empties all files and subdirectories in the specified directory.
     * 
     * @param {string} directoryPath - The path to the directory whose contents are to be emptied.
     * @returns {void | Error} - Returns nothing if successful, otherwise returns an Error.
     */
    
    try {
        // Check if the directory exists
        if (!fs.existsSync(directoryPath)) {
            throw new Error(`The specified path ${directoryPath} does not exist.`);
        }

        // Read the directory contents
        const files = fs.readdirSync(directoryPath);

        // Loop through each file and remove it
        for (const file of files) {
            const filePath = path.join(directoryPath, file);
            
            // Check if the item is a file or directory and remove accordingly
            if (fs.lstatSync(filePath).isFile()) {
                fs.unlinkSync(filePath);
            } else if (fs.lstatSync(filePath).isDirectory()) {
                emptyDirectory(filePath); // Recursively empty subdirectories
                fs.rmdirSync(filePath);
            }
        }
        
        console.log('Directory has been emptied successfully.');
    } catch (error) {
        return error;
    }
}