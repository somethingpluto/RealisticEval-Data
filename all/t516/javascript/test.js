describe('TestReadYaml', () => {
    let validYamlFile = 'test_valid.yaml';
    let invalidYamlFile = 'test_invalid.yaml';
    let nonExistentFile = 'non_existent.yaml';

    beforeAll(() => {
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
        if (fs.existsSync(validYamlFile)) {
            fs.unlinkSync(validYamlFile);
        }
        if (fs.existsSync(invalidYamlFile)) {
            fs.unlinkSync(invalidYamlFile);
        }
    });

    describe('test_read_valid_yaml', () => {
        it('should correctly parse a valid YAML file', () => {
            const expectedData = {
                name: 'Example',
                version: 1.0,
                dependencies: ['package1', 'package2']
            };
            const result = readYaml(validYamlFile);
            expect(result).toEqual(expectedData);
        });
    });

    describe('test_file_not_found', () => {
        it('should throw an error when the file does not exist', () => {
            expect(() => readYaml(nonExistentFile)).toThrow(/The file 'non_existent\.yaml' does not exist/);
        });
    });

    describe('test_empty_yaml_file', () => {
        let emptyYamlFile = 'test_empty.yaml';

        beforeAll(() => {
            fs.writeFileSync(emptyYamlFile, '');
        });

        afterAll(() => {
            if (fs.existsSync(emptyYamlFile)) {
                fs.unlinkSync(emptyYamlFile);
            }
        });

        it('should return null for an empty YAML file', () => {
            const result = readYaml(emptyYamlFile);
            expect(result).toBeNull();
        });
    });
});