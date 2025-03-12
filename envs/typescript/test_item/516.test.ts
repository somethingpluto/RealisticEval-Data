import * as fs from 'fs';
import * as yaml from 'js-yaml';
import { join } from 'path';

/**
 * Reads a YAML file and returns its content as a JavaScript object.
 *
 * @param filePath - The path to the YAML file.
 * @returns Parsed YAML content as a JavaScript data structure.
 * @throws {Error} If the specified file does not exist or there is an error parsing the YAML file.
 */
function readYaml(filePath: string): object {
    try {
        const doc = yaml.load(fs.readFileSync(join(__dirname, filePath), 'utf8'));
        return doc;
    } catch (e) {
        throw new Error(`Error reading or parsing YAML file: ${filePath}`);
    }
}
describe('TestReadYaml', () => {
    let validYamlFile: string;
    let invalidYamlFile: string;
    let nonExistentFile: string;

    beforeAll(() => {
        // Create a temporary YAML file for testing
        validYamlFile = 'test_valid.yaml';
        invalidYamlFile = 'test_invalid.yaml';
        nonExistentFile = 'non_existent.yaml';

        // Valid YAML content
        fs.writeFileSync(validYamlFile, `
            name: Example
            version: 1.0
            dependencies:
              - package1
              - package2
        `);

        // Invalid YAML content
        fs.writeFileSync(invalidYamlFile, `
            name: Example
            version: 1.0
            dependencies:
              - package1
              - package2
            invalid_yaml:
              -
        `);
    });

    afterAll(() => {
        // Remove the temporary YAML files after testing
        if (fs.existsSync(validYamlFile)) {
            fs.unlinkSync(validYamlFile);
        }
        if (fs.existsSync(invalidYamlFile)) {
            fs.unlinkSync(invalidYamlFile);
        }
    });

    it('should read a valid YAML file correctly', () => {
        const expectedData = {
            name: 'Example',
            version: 1.0,
            dependencies: ['package1', 'package2']
        };

        const result = readYaml(validYamlFile);
        expect(result).toEqual(expectedData);
    });

    it('should throw an error when the file does not exist', () => {
        expect(() => readYaml(nonExistentFile)).toThrow(/The file 'non_existent\.yaml' does not exist/);
    });

    it('should handle an empty YAML file', () => {
        const emptyYamlFile = 'test_empty.yaml';
        fs.writeFileSync(emptyYamlFile, ''); // Create an empty YAML file

        const result = readYaml(emptyYamlFile);
        expect(result).toBeNull(); // Expecting null for empty file

        fs.unlinkSync(emptyYamlFile); // Cleanup after the test
    });
});
