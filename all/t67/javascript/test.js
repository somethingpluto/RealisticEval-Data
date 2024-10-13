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