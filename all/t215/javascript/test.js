describe('replaceWordsInFile', () => {
    it('should replace words in the file according to the replacement dictionary', async () => {
      const filePath = 'path/to/your/testfile.txt';
      const replacementDict = { 'hello': 'hi', 'world': 'earth' };
  
      // Mock the readFile method to return a sample text
      jest.spyOn(fs, 'readFile').mockResolvedValue('hello world');
  
      const result = await replaceWordsInFile(filePath, replacementDict);
  
      expect(result).toBe('hi earth');
  
      // Restore the original readFile method
      fs.readFile.mockRestore();
    });
  });