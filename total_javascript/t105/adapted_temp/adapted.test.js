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

// Test Cases

// Test Case 1: Basic functionality with a small memory section
const buffer1 = new ArrayBuffer(128); // 64 words
const view1 = new DataView(buffer1);
view1.setUint16(0, 0b1111100000000000); // Red
view1.setUint16(2, 0b0000011111100000); // Green
view1.setUint16(4, 0b0000000000011111); // Blue
const canvas1 = createMemoryVisualizer(view1, 0, 3, 2, 2, 2);
document.body.appendChild(canvas1); // Expected: 2x2 blocks, Red, Green, Blue, Black

// Test Case 2: Larger memory section with varied colors
const buffer2 = new ArrayBuffer(512); // 256 words
const view2 = new DataView(buffer2);
for (let i = 0; i < 256; i++) {
    view2.setUint16(i * 2, i); // Varying colors
}
const canvas2 = createMemoryVisualizer(view2, 0, 255, 16, 16, 2);
document.body.appendChild(canvas2); // Expected: A gradient of colors

// Test Case 3: Full memory visualization (simple)
const buffer3 = new ArrayBuffer(65536); // 32768 words
const view3 = new DataView(buffer3);
for (let i = 0; i < 32768; i++) {
    view3.setUint16(i * 2, i); // Varying colors
}
const canvas3 = createMemoryVisualizer(view3, 0, 32767, 64, 512, 2);
document.body.appendChild(canvas3); // Expected: Large gradient visualization

// Test Case 4: Non-sequential memory section
const buffer4 = new ArrayBuffer(128); // 64 words
const view4 = new DataView(buffer4);
view4.setUint16(0, 0b0000011111100000); // Green
view4.setUint16(10, 0b1111100000000000); // Red
view4.setUint16(20, 0b0000000000011111); // Blue
const canvas4 = createMemoryVisualizer(view4, 0, 20, 8, 8, 2);
document.body.appendChild(canvas4); // Expected: Mostly black with some colors

// Test Case 5: Minimal input (single word)
const buffer5 = new ArrayBuffer(2); // 1 word
const view5 = new DataView(buffer5);
view5.setUint16(0, 0b1111100000000000); // Red
const canvas5 = createMemoryVisualizer(view5, 0, 0, 1, 1, 2);
document.body.appendChild(canvas5); // Expected: 2x2 red block
