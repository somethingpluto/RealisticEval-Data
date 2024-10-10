import { createCanvas, loadImage } from 'canvas';

/**
 * Count the number of unique colors in an image.
 *
 * @param image_path - Path to the image file.
 * @returns The number of unique colors in the image.
 */
async function countUniqueColors(imagePath: string): Promise<number> {
    const canvas = createCanvas(1, 1);
    const ctx = canvas.getContext('2d');
    
    // Load the image into the canvas
    await loadImage(imagePath).then((image) => {
        canvas.width = image.width;
        canvas.height = image.height;
        ctx.drawImage(image, 0, 0);
    });

    const imageData = ctx.getImageData(0, 0, canvas.width, canvas.height);
    const data = imageData.data;

    const colorSet = new Set<string>();

    for (let i = 0; i < data.length; i += 4) {
        const r = data[i];
        const g = data[i + 1];
        const b = data[i + 2];
        const a = data[i + 3];

        // Create a color string in the format "rgba(r,g,b,a)"
        const color = `rgba(${r},${g},${b},${a})`;
        colorSet.add(color);
    }

    return colorSet.size;
}