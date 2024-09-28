const { xmlToDataFrame } = require('./yourModule'); // Adjust the import based on your module
const pandas = require('pandas-js');

describe('xmlToDataFrame', () => {
    it('should handle a single sequence', async () => {
        const xmlData = `<root>
                            <sequence>
                                <name>John</name>
                                <age>30</age>
                            </sequence>
                         </root>`;
        const df = await xmlToDataFrame(Buffer.from(xmlData)); // Using Buffer to simulate input
        const expected = new pandas.DataFrame([{'name': 'John', 'age': '30'}]);
        expect(df.toString()).toEqual(expected.toString());
    });

    it('should handle multiple sequences', async () => {
        const xmlData = `<root>
                            <sequence>
                                <name>Alice</name>
                                <age>25</age>
                            </sequence>
                            <sequence>
                                <name>Bob</name>
                                <age>22</age>
                            </sequence>
                         </root>`;
        const df = await xmlToDataFrame(Buffer.from(xmlData));
        const expected = new pandas.DataFrame([{'name': 'Alice', 'age': '25'}, {'name': 'Bob', 'age': '22'}]);
        expect(df.toString()).toEqual(expected.toString());
    });

    it('should handle an empty sequence', async () => {
        const xmlData = `<root>
                            <sequence></sequence>
                         </root>`;
        const df = await xmlToDataFrame(Buffer.from(xmlData));
        const expected = new pandas.DataFrame([{}]);
        expect(df.toString()).toEqual(expected.toString());
    });

    it('should handle mixed content', async () => {
        const xmlData = `<root>
                            <sequence>
                                <name>Chris</name>
                            </sequence>
                            <sequence>
                                <age>28</age>
                            </sequence>
                         </root>`;
        const df = await xmlToDataFrame(Buffer.from(xmlData));
        const expected = new pandas.DataFrame([{'name': 'Chris', 'age': null}, {'name': null, 'age': '28'}]);
        expect(df.toString()).toEqual(expected.toString());
    });

    it('should handle no sequences', async () => {
        const xmlData = `<root></root>`;
        const df = await xmlToDataFrame(Buffer.from(xmlData));
        const expected = new pandas.DataFrame();
        expect(df.toString()).toEqual(expected.toString());
    });
});