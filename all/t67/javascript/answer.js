const xml2js = require('xml2js');
const fs = require('fs');

function parseXamlToDict(xamlFile) {
    /**
     * Parse a XAML file and extract key-value pairs from 'String' elements.
     *
     * @param {string} xamlFile - Path to the XAML file.
     * @returns {Object} A dictionary containing the key-value pairs extracted from 'String' elements.
     */
    try {
        // Read the XAML file
        const xamlContent = fs.readFileSync(xamlFile, 'utf8');

        // Parse the XAML content
        const parser = new xml2js.Parser();
        parser.parseString(xamlContent, (err, result) => {
            if (err) {
                console.error(`Error parsing the XAML file: ${err}`);
                return {};
            }

            // Dictionary to hold the key-value pairs
            const resultDict = {};

            // Iterate through all 'String' elements in the XAML file
            if (result && result.root && Array.isArray(result.root.String)) {
                result.root.String.forEach((stringElement) => {
                    const key = stringElement.$.Key;
                    if (key) {
                        if (!stringElement._ || stringElement._ === '') {
                            resultDict[key] = "";
                        } else {
                            resultDict[key] = stringElement._;
                        }
                    }
                });
            }

            return resultDict;
        });

    } catch (error) {
        if (error.code === 'ENOENT') {
            console.error(`Error: The file ${xamlFile} does not exist.`);
            return {};
        } else {
            console.error(`Error parsing the XAML file: ${error.message}`);
            return {};
        }
    }
}