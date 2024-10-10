function replaceWordsInFile(filePath, replacementDict) {
    /*
     * Read a text file, replace words according to a dictionary map, and return the modified text.
     *
     * @param {string} filePath - The path to the text file.
     * @param {Object} replacementDict - A dictionary where the keys are words to be replaced, and the values are the replacement words.
     * @return {string} The text with the words replaced.
     */
    
    // Node.js fs module for reading files
    const fs = require('fs');

    // Read the file synchronously
    let data = fs.readFileSync(filePath, 'utf8');
    
    // Iterate over each key-value pair in the replacement dictionary
    for(let oldWord in replacementDict){
        if(replacementDict.hasOwnProperty(oldWord)){
            let newWord = replacementDict[oldWord];
            // Replace all occurrences of old word with new word
            data = data.split(oldWord).join(newWord);
        }
    }

    // Return the modified text
    return data;
}