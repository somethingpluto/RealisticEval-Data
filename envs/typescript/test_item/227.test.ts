import { createCanvas, loadImage } from 'canvas';
import { promisify } from 'util';

const readFile = promisify(require('fs').readFile);
const writeFile = promisify(require('fs').writeFile);

async function countUniqueColors(imagePath: string): Promise<number> {
  try {
    const buffer = await readFile(imagePath);
    const image = await loadImage(buffer);
    const canvas = createCanvas(image.width, image.height);
    const ctx = canvas.getContext('2d');
    ctx.drawImage(image, 0, 0);
    const imageData = ctx.getImageData(0, 0, image.width, image.height);
    const colors = new Set<string>();

    for (let i = 0; i < imageData.data.length; i += 4) {
      const color = `${imageData.data[i]}${imageData.data[i + 1]}${imageData.data[i + 2]}`;
      colors.add(color);
    }

    return colors.size;
  } catch (error) {
    console.error('Error processing image:', error);
    throw error;
  }
}
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
