import fs from 'fs';

function replaceWordsInFile(filePath: string, replacementDict: { [key: string]: string }): string {
    /**
     * Read a text file, replace words according to a dictionary map, and return the modified text.
     *
     * Parameters:
     * - filePath (string): The path to the text file.
     * - replacementDict (object): An object where the keys are words to be replaced, and the values are the replacement words.
     *
     * Returns:
     * - string: The text with the words replaced or an error message.
     */

    try {
        // Read the content of the file
        const text = fs.readFileSync(filePath, 'utf8');

        // Replace words according to the replacement dictionary
        for (const oldWord in replacementDict) {
            if (replacementDict.hasOwnProperty(oldWord)) {
                const newWord = replacementDict[oldWord];
                text.replace(new RegExp(oldWord, 'g'), newWord);
            }
        }

        return text;

    } catch (error) {
        if (error instanceof Error && error.code === 'ENOENT') {
            return "Error: The file was not found.";
        }
        return `Error: ${error.message}`;
    }
}