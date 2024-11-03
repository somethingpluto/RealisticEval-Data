import fs from 'fs'
function findAndReplaceInFile(filePath, searchString, replaceString) {
    /** 
     * Finds and replaces text in a specified file.
     *
     * @param {string} filePath - The path to the file.
     * @param {string} searchString - The string to search for.
     * @param {string} replaceString - The string to replace with.
     * @throws {Error} If an I/O error occurs reading from the file or writing to the file.
     */
    try {
        // Read the content of the file
        let fileContent = fs.readFileSync(filePath, { encoding: 'utf-8' });

        // Replace the search string with the replacement string
        let replacedContent = fileContent.replace(new RegExp(searchString, 'g'), replaceString);

        // Write the replaced content back to the file
        fs.writeFileSync(filePath, replacedContent, { encoding: 'utf-8' });
    } catch (error) {
        console.error(`Error occurred: ${error.message}`);
    }
}