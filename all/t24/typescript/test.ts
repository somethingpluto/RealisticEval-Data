describe('TestConvertYamlToJson', () => {
    let simpleYaml: string;
    let nestedYaml: string;
    let emptyYaml: string;
    let listYaml: string;
    let invalidYaml: string;
  
    beforeEach(() => {
      // Create temporary YAML files for testing
      simpleYaml = 'simple.yaml';
      nestedYaml = 'nested.yaml';
      emptyYaml = 'empty.yaml';
      listYaml = 'list.yaml';
      invalidYaml = 'invalid.yaml';
  
      fs.writeFileSync(simpleYaml, "name: John Doe\nage: 30\n");
      fs.writeFileSync(nestedYaml, "person:\n  name: Jane Doe\n  age: 25\n  address:\n    city: New York\n    zip: 10001\n");
      fs.writeFileSync(emptyYaml, "");
      fs.writeFileSync(listYaml, "- item1\n- item2\n- item3\n");
      fs.writeFileSync(invalidYaml, "{ invalid: YAML: structure }\n");
    });
  
    afterEach(() => {
      // Remove temporary files after testing
      fs.unlinkSync(simpleYaml);
      fs.unlinkSync(nestedYaml);
      fs.unlinkSync(emptyYaml);
      fs.unlinkSync(listYaml);
      fs.unlinkSync(invalidYaml);
  
      if (fs.existsSync('output.json')) {
        fs.unlinkSync('output.json');
      }
    });
  
    it('should correctly convert simple YAML to JSON', () => {
      convertYamlToJson(simpleYaml, 'output.json');
      const data = JSON.parse(fs.readFileSync('output.json', 'utf-8'));
      expect(data).toEqual({ name: 'John Doe', age: 30 });
    });
  
    it('should correctly convert nested YAML to JSON', () => {
      convertYamlToJson(nestedYaml, 'output.json');
      const data = JSON.parse(fs.readFileSync('output.json', 'utf-8'));
      const expectedData = {
        person: {
          name: 'Jane Doe',
          age: 25,
          address: {
            city: 'New York',
            zip: 10001
          }
        }
      };
      expect(data).toEqual(expectedData);
    });
  
    it('should correctly handle empty YAML conversion', () => {
      convertYamlToJson(emptyYaml, 'output.json');
      const data = JSON.parse(fs.readFileSync('output.json', 'utf-8'));
      expect(data).toBeNull();
    });
  
    it('should correctly convert list YAML to JSON', () => {
      convertYamlToJson(listYaml, 'output.json');
      const data = JSON.parse(fs.readFileSync('output.json', 'utf-8'));
      expect(data).toEqual(['item1', 'item2', 'item3']);
    });
  
    it('should throw an error when converting invalid YAML', () => {
      expect(() => convertYamlToJson(invalidYaml, 'output.json')).toThrowErrorMatchingInlineSnapshot(`"YAMLException: while parsing a flow scalar\\n  in \\"<unicode string>\\", line 1, column 1:\\n    { invalid: YAML: structure }\\n    ^\\nexpected \\'<<\\', but found \\'{\\'\\n  in \\"<unicode string>\\", line 1, column 2:\\n    { invalid: YAML: structure }\\n      ^\\"`);
    });
  });