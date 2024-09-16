/**
 * Creates a canvas element that visualizes a section of memory as 16x16 pixel blocks.
 * Each 16-bit word in the DataView is represented by a 2x2 pixel block using RGB565 encoding.
 *
 * @param {DataView} memory - The DataView representing the memory to visualize.
 * @param {number} startWordInclusive - The starting word index (inclusive).
 * @param {number} endWordInclusive - The ending word index (inclusive).
 * @param {number} wordsPerRow - The number of words per visual row.
 * @param {number} totalRows - The total number of visual rows.
 * @param {number} pixelSize - The size of each visualized word in pixels (e.g., 2 for 2x2 blocks).
 * @returns {HTMLCanvasElement} - The canvas element with the memory visualization.
 */
function createMemoryVisualizer(memory, startWordInclusive, endWordInclusive, wordsPerRow, totalRows, pixelSize) {
    const canvas = document.createElement('canvas');
    canvas.width = wordsPerRow * pixelSize;
    canvas.height = totalRows * pixelSize;

    const ctx = canvas.getContext('2d');
    if (!ctx) {
        throw new Error('Unable to get 2D context for canvas.');
    }

    const imageData = ctx.createImageData(canvas.width, canvas.height);

    for (let i = startWordInclusive; i <= endWordInclusive; i++) {
        const word = memory.getUint16(i * 2);
        const red = (word >> 11) & 0x1F;
        const green = (word >> 5) & 0x3F;
        const blue = word & 0x1F;

        const r = red << 3;       // Convert 5-bit red to 8-bit
        const g = green << 2;     // Convert 6-bit green to 8-bit
        const b = blue << 3;      // Convert 5-bit blue to 8-bit

        const row = Math.floor(i / wordsPerRow);
        const col = i % wordsPerRow;
        const blockX = col * pixelSize;
        const blockY = row * pixelSize;

        for (let y = 0; y < pixelSize; y++) {
            for (let x = 0; x < pixelSize; x++) {
                const pixelX = blockX + x;
                const pixelY = blockY + y;
                const pixelOffset = (pixelY * canvas.width + pixelX) * 4;

                imageData.data[pixelOffset] = r;
                imageData.data[pixelOffset + 1] = g;
                imageData.data[pixelOffset + 2] = b;
                imageData.data[pixelOffset + 3] = 255; // Fully opaque
            }
        }
    }

    ctx.putImageData(imageData, 0, 0);
    return canvas;
}
