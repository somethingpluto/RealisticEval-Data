describe('countUniqueColors', () => {
    it('should return the correct number of unique colors in an image', async () => {
      const imagePath = path.join(__dirname, 'test-image.jpg'); // Replace with your test image path
  
      if (!fs.existsSync(imagePath)) {
        throw new Error(`Image not found at ${imagePath}`);
      }
  
      const result = await countUniqueColors(imagePath);
      
      // Replace with expected value based on your image
      expect(result).toBe(10); 
    });
  });