describe('compareFiles', () => {
    it('should return empty array when both files are identical', async () => {
      const tempFilePath = './tempFile.txt';
      fs.writeFileSync(tempFilePath, 'This is a test file.');
  
      const result = await compareFiles(tempFilePath, tempFilePath);
  
      expect(result).toEqual([]);
      fs.unlinkSync(tempFilePath);
    });
  
    it('should return differences when files are different', async () => {
      const tempFilePath1 = './tempFile1.txt';
      const tempFilePath2 = './tempFile2.txt';
      
      fs.writeFileSync(tempFilePath1, 'This is a test file.');
      fs.writeFileSync(tempFilePath2, 'This is another test file.');
  
      const result = await compareFiles(tempFilePath1, tempFilePath2);
  
      expect(result.length).toBeGreaterThan(0);
      fs.unlinkSync(tempFilePath1);
      fs.unlinkSync(tempFilePath2);
    });
  });