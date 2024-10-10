function extractParseDictionaries(filePath) {
    /**
     * Extract and parse strings containing Python dictionary syntax from a given file
     * @param {string} filePath - The path to the file from which to extract dictionary strings.
     * 
     * @returns {Array<Object>} - A list of dictionaries extracted and parsed from the file.
     */

    try {
        const data = fs.readFileSync(filePath, 'utf8');
        let dictStrings = data.match(/\{.*?\}/g); // Match any string that looks like a Python dictionary

        if (!dictStrings) return [];

        return dictStrings.map(dictString => JSON.parse(dictString.replace(/'/g, '"')));
    } catch (error) {
        console.error(`Error reading or parsing ${filePath}:`, error);
        return [];
    }
}