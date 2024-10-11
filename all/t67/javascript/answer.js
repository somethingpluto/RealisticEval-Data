const fs = require('fs');
const path = require('path');

function parseXamlToDict(xamlFilePath) {
    /**
     * Parse the XAML file, extract the key-value pairs within the String element, and return the model_answer_result in a dictionary
     * @param {string} xamlFilePath - Path to the XAML file.
     * @returns {Object} - A dictionary containing the key-value pairs extracted from 'String' elements.
     */

    // Read the content of the XAML file
    const xamlContent = fs.readFileSync(xamlFilePath, 'utf8');

    // Regular expression to match <String> tags and their content
    const stringRegex = /<String>(.*?)<\/String>/g;
    let match;

    const result = {};

    // Extract key-value pairs using regex
    while ((match = stringRegex.exec(xamlContent)) !== null) {
        // Assuming the content inside <String> tag is in the format "key=value"
        const keyValue = match[1].trim();
        const [key, value] = keyValue.split('=');
        if (key && value) {
            result[key.trim()] = value.trim();
        }
    }

    return result;
}