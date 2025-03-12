const fs = require('fs');
const path = require('path');
const { createCanvas, loadImage } = require('canvas');

/**
 * Count the number of unique colors in an image.
 *
 * @param {string} imagePath - Path to the image file.
 * @returns {number} The number of unique colors in the image.
 */
async function countUniqueColors(imagePath) {
    try {
        // Load the image
        const image = await loadImage(imagePath);

        // Create a canvas with the same dimensions as the image
        const canvas = createCanvas(image.width, image.height);
        const ctx = canvas.getContext('2d');

        // Draw the image onto the canvas
        ctx.drawImage(image, 0, 0);

        // Get the image data
        const imageData = ctx.getImageData(0, 0, image.width, image.height).data;

        // Create a Set to store unique colors
        const uniqueColors = new Set();

        // Iterate over the image data and extract colors
        for (let i = 0; i < imageData.length; i += 4) {
            const r = imageData[i];
            const g = imageData[i + 1];
            const b = imageData[i + 2];
            const a = imageData[i + 3];

            // Create a unique key for the color
            const colorKey = `${r},${g},${b},${a}`;

            // Add the color key to the Set
            uniqueColors.add(colorKey);
        }

        // Return the number of unique colors
        return uniqueColors.size;
    } catch (error) {
        console.error('Error processing image:', error);
        throw error;
    }
}

module.exports = countUniqueColors;
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
