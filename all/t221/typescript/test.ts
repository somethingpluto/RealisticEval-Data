describe('extractParseDicts', () => {
    it('should return an empty array when no dict strings are found in the file', () => {
      const filePath = 'path_to_your_file.txt'; // Replace with your actual file path
      expect(extractParseDicts(filePath)).toEqual([]);
    });
  
    it('should correctly parse a single dict string from the file', () => {
      const filePath = 'path_to_your_file.txt'; // Replace with your actual file path
      const expectedOutput = [{ key: 'value' }];
      writeFileSync(filePath, JSON.stringify(expectedOutput));
      expect(extractParseDicts(filePath)).toEqual(expectedOutput);
    });
  
    it('should correctly parse multiple dict strings from the file', () => {
      const filePath = 'path_to_your_file.txt'; // Replace with your actual file path
      const expectedOutput = [
        { key1: 'value1' },
        { key2: 'value2' }
      ];
      writeFileSync(filePath, JSON.stringify(expectedOutput));
      expect(extractParseDicts(filePath)).toEqual(expectedOutput);
    });
  });