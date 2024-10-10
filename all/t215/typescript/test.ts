describe('replaceWordsInFile', () => {
    const testFilePath = 'test-file.txt';
  
    beforeEach(() => {
      // Create a test file with some initial content
      fs.writeFileSync(testFilePath, 'hello world');
    });
  
    afterEach(() => {
      // Clean up after each test
      if (fs.existsSync(testFilePath)) {
        fs.unlinkSync(testFilePath);
      }
    });
  
    it('should replace words in the file', async () => {
      const replacementDict = {
        hello: 'hi',
        world: 'earth'
      };
  
      await replaceWordsInFile(testFilePath, replacementDict);
  
      const updatedContent = fs.readFileSync(testFilePath, 'utf8');
      expect(updatedContent).toBe('hi earth');
    });
  });