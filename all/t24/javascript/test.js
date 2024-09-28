const fs = require('fs');
const yaml = require('js-yaml');
const { convertYamlToJson } = require('./yourModule');  // Replace with your actual module

describe('TestConvertYamlToJson', () => {
    const testFiles = {
        simple: 'simple.yaml',
        nested: 'nested.yaml',
        empty: 'empty.yaml',
        list: 'list.yaml',
        invalid: 'invalid.yaml',
        output: 'output.json'
    };

    beforeAll(() => {
        // Create temporary YAML files for testing
        fs.writeFileSync(testFiles.simple, "name: John Doe\nage: 30\n", 'utf8');
        fs.writeFileSync(testFiles.nested, "person:\n  name: Jane Doe\n  age: 25\n  address:\n    city: New York\n    zip: 10001\n", 'utf8');
        fs.writeFileSync(testFiles.empty, "", 'utf8');
        fs.writeFileSync(testFiles.list, "- item1\n- item2\n- item3\n", 'utf8');
        fs.writeFileSync(testFiles.invalid, "{ invalid: YAML: structure }\n", 'utf8');
    });

    afterAll(() => {
        // Remove temporary files after testing
        Object.values(testFiles).forEach(file => {
            if (fs.existsSync(file)) {
                fs.unlinkSync(file);
            }
        });
    });

    test('simple yaml conversion', () => {
        convertYamlToJson(testFiles.simple, testFiles.output);
        const data = JSON.parse(fs.readFileSync(testFiles.output, 'utf8'));
        expect(data).toEqual({ name: "John Doe", age: 30 });
    });

    test('nested yaml conversion', () => {
        convertYamlToJson(testFiles.nested, testFiles.output);
        const data = JSON.parse(fs.readFileSync(testFiles.output, 'utf8'));
        const expectedData = {
            person: {
                name: "Jane Doe",
                age: 25,
                address: {
                    city: "New York",
                    zip: 10001
                }
            }
        };
        expect(data).toEqual(expectedData);
    });

    test('empty yaml conversion', () => {
        convertYamlToJson(testFiles.empty, testFiles.output);
        const data = JSON.parse(fs.readFileSync(testFiles.output, 'utf8'));
        expect(data).toEqual(null);
    });

    test('list yaml conversion', () => {
        convertYamlToJson(testFiles.list, testFiles.output);
        const data = JSON.parse(fs.readFileSync(testFiles.output, 'utf8'));
        expect(data).toEqual(["item1", "item2", "item3"]);
    });

    test('invalid yaml conversion', () => {
        expect(() => {
            convertYamlToJson(testFiles.invalid, testFiles.output);
        }).toThrow(yaml.YAMLError);
    });
});