import * as fs from 'fs';
import * as xml2js from 'xml2js';

/**
 * Parse a XAML file and extract key-value pairs from 'String' elements.
 *
 * @param xamlFile - Path to the XAML file.
 * @returns A dictionary containing the key-value pairs extracted from 'String' elements.
 */
function parseXamlToDict(xamlFile: string): Record<string, string> {
    try {
        // Read the XAML file
        const xamlContent = fs.readFileSync(xamlFile, 'utf-8');

        // Parse the XAML content
        const parser = new xml2js.Parser();
        let result: any;
        parser.parseString(xamlContent, (err, res) => {
            if (err) {
                console.error(`Error parsing the XAML file: ${err}`);
                result = {};
            } else {
                result = res;
            }
        });

        // Wait for the asynchronous parsing to complete
        while (!result) {}

        // Dictionary to hold the key-value pairs
        const resultDict: Record<string, string> = {};

        // Iterate through all 'String' elements in the XAML file
        if (result.ResourceDictionary && result.ResourceDictionary.String) {
            const stringElements = Array.isArray(result.ResourceDictionary.String)
                ? result.ResourceDictionary.String
                : [result.ResourceDictionary.String];

            for (const stringElement of stringElements) {
                const key = stringElement['@_Key'];
                if (key) {
                    const value = stringElement._ ? String(stringElement._) : '';
                    resultDict[key] = value;
                }
            }
        }

        return resultDict;

    } catch (error) {
        if (error.code === 'ENOENT') {
            console.error(`Error: The file ${xamlFile} does not exist.`);
            return {};
        } else {
            console.error(`Error parsing the XAML file: ${error}`);
            return {};
        }
    }
}