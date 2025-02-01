/**
 * Count the number of unique colors in an image.
 *
 * @param {string} imagePath - Path to the image file.
 * @returns {number} The number of unique colors in the image.
 */
function countUniqueColors(imagePath) {
    return new Promise((resolve, reject) => {
        const img = new Image();
        img.crossOrigin = "Anonymous";
        img.onload = () => {
            const canvas = document.createElement('canvas');
            const ctx = canvas.getContext('2d');
            canvas.width = img.width;
            canvas.height = img.height;
            ctx.drawImage(img, 0, 0);
            const imageData = ctx.getImageData(0, 0, canvas.width, canvas.height);
            const pixels = imageData.data;
            const uniqueColors = new Set();

            for (let i = 0; i < pixels.length; i += 4) {
                const r = pixels[i];
                const g = pixels[i + 1];
                const b = pixels[i + 2];
                const a = pixels[i + 3];
                if (a > 0) { // Ignore transparent pixels
                    uniqueColors.add(`${r},${g},${b}`);
                }
            }

            resolve(uniqueColors.size);
        };
        img.onerror = (error) => {
            reject(error);
        };
        img.src = imagePath;
    });
}
describe('countUniqueColors', () => {
    it('should return the number of unique colors in an image', async () => {
      // Mock the image path and expected result
      const imagePath = 'path/to/image.jpg';
      const expectedResult = 10; // Replace with the actual expected result
  
      // Call the function with the mock image path
      const result = await countUniqueColors(imagePath);
  
      // Assert that the result matches the expected result
      expect(result).toBe(expectedResult);
    });
  
    it('should handle cases where the image has no colors', async () => {
      // Mock the image path and expected result
      const imagePath = 'path/to/empty-image.jpg';
      const expectedResult = 0; // Replace with the actual expected result
  
      // Call the function with the mock image path
      const result = await countUniqueColors(imagePath);
  
      // Assert that the result matches the expected result
      expect(result).toBe(expectedResult);
    });
  });
