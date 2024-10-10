describe('TSV to JSONL Conversion', () => {
    const tsvFilePath = join(__dirname, '__mocks__', 'example.tsv');
    const jsonlFilePath = join(__dirname, '__mocks__', 'output.jsonl');
  
    beforeAll(() => {
      // Create a mock TSV file for testing
      writeFileSync(tsvFilePath, 'column1\tcolumn2\nvalue1\tvalue2');
    });
  
    afterAll(() => {
      // Clean up the mock files
      try {
        unlinkSync(tsvFilePath);
        unlinkSync(jsonlFilePath);
      } catch (error) {
        console.error(`Error cleaning up mock files: ${error}`);
      }
    });
  
    it('should convert TSV to JSONL successfully', async () => {
      await tsvToJsonl(tsvFilePath, jsonlFilePath);
  
      const expectedJsonlContent = 'column1,column2\nvalue1,value2\n';
      const actualJsonlContent = readFileSync(jsonlFilePath, 'utf-8');
  
      expect(actualJsonlContent).toBe(expectedJsonlContent);
    });
  });