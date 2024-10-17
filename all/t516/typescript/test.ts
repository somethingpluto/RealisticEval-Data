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