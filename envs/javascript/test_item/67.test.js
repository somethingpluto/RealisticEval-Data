/**
 * Parses a XAML file, extracts the key-value pairs within the 'String' elements, and returns the result in a dictionary.
 * @param {string} xamlFile - Path to the XAML file.
 * @returns {Object} A dictionary containing the key-value pairs extracted from 'String' elements.
 */
function parseXamlToDict(xamlFile) {
    return fetch(xamlFile)
        .then(response => response.text())
        .then(xamlText => {
            const parser = new DOMParser();
            const xmlDoc = parser.parseFromString(xamlText, "text/xml");
            const stringElements = xmlDoc.getElementsByTagName("String");

            const result = {};
            for (let i = 0; i < stringElements.length; i++) {
                const key = stringElements[i].getAttribute("Key");
                const value = stringElements[i].textContent;
                if (key) {
                    result[key] = value;
                }
            }

            return result;
        })
        .catch(error => {
            console.error("Error parsing XAML file:", error);
            return {};
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
