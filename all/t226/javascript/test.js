describe('tsvToJsonl', () => {
    const tsvPath = 'path/to/test.tsv';
    const jsonlPath = 'path/to/test.jsonl';
  
    beforeEach(() => {
      jest.clearAllMocks();
    });
  
    it('should convert tsv to jsonl', async () => {
      // Mock the readFileSync and writeFileSync functions
      fs.readFileSync.mockReturnValueOnce('column1\tcolumn2\nvalue1\tvalue2');
      fs.writeFileSync.mockImplementation((filePath, data) => {
        expect(filePath).toBe(jsonlPath);
        expect(data).toBe(JSON.stringify([{ column1: 'value1', column2: 'value2' }], null, 2));
      });
  
      await convert.tsvToJsonl(tsvPath, jsonlPath);
  
      expect(fs.readFileSync).toHaveBeenCalledWith(tsvPath, 'utf8');
      expect(fs.writeFileSync).toHaveBeenCalled();
    });
  });