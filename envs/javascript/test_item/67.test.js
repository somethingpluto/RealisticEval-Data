const fs = require('fs');
const xml2js = require('xml2js');

/**
 * Parses a XAML file, extracts the key-value pairs within the 'String' elements, and returns the result in a dictionary.
 * @param {string} xamlFile - Path to the XAML file.
 * @returns {Object} A dictionary containing the key-value pairs extracted from 'String' elements.
 */
function parseXamlToDict(xamlFile) {
    return new Promise((resolve, reject) => {
        // Read the XAML file
        fs.readFile(xamlFile, 'utf8', (err, data) => {
            if (err) {
                reject(err);
                return;
            }

            // Parse the XML content
            xml2js.parseString(data, { explicitArray: false }, (parseErr, result) => {
                if (parseErr) {
                    reject(parseErr);
                    return;
                }

                const dict = {};

                // Extract the 'String' elements
                if (result.ResourceDictionary && result.ResourceDictionary.String) {
                    const strings = result.ResourceDictionary.String;

                    // Handle both single and multiple 'String' elements
                    if (Array.isArray(strings)) {
                        strings.forEach(string => {
                            if (string.$.Key && string._) {
                                dict[string.$.Key] = string._;
                            }
                        });
                    } else if (strings.$.Key && strings._) {
                        dict[strings.$.Key] = strings._;
                    }
                }

                resolve(dict);
            });
        });
    });
}
const { parse } = require('xml2js');

describe('TestParseXamlToDict', () => {
    it('should correctly parse valid strings', () => {
        const xamlData = `
            <root>
                <String Key="Username">Alice</String>
                <String Key="Password">secret</String>
            </root>
        `;
        const expected = { Username: 'Alice', Password: 'secret' };
        const result = parseXamlToDict(xamlData);
        expect(result).toEqual(expected);
    });

    it('should handle missing key attribute', () => {
        const xamlData = `
            <root>
                <String>Alice</String>
            </root>
        `;
        const expected = {};
        const result = parseXamlToDict(xamlData);
        expect(result).toEqual(expected);
    });

    it('should handle no string tags', () => {
        const xamlData = `
            <root>
                <Data>Some question</Data>
            </root>
        `;
        const expected = {};
        const result = parseXamlToDict(xamlData);
        expect(result).toEqual(expected);
    });

    it('should correctly parse nested string tags', () => {
        const xamlData = `
            <root>
                <Container>
                    <String Key="Username">Bob</String>
                </Container>
                <String Key="Location">Earth</String>
            </root>
        `;
        const expected = { Username: 'Bob', Location: 'Earth' };
        const result = parseXamlToDict(xamlData);
        expect(result).toEqual(expected);
    });
});
