describe('createMemoryVisualizer', () => {
    // Cleanup DOM after each test
    afterEach(() => {
        document.body.innerHTML = ''; // Clear the DOM
    });

    test('Test Case 1: Basic functionality with a small memory section', () => {
        const buffer1 = new ArrayBuffer(128); // 64 words
        const view1 = new DataView(buffer1);
        view1.setUint16(0, 0b1111100000000000); // Red
        view1.setUint16(2, 0b0000011111100000); // Green
        view1.setUint16(4, 0b0000000000011111); // Blue

        const canvas1 = createMemoryVisualizer(view1, 0, 3, 2, 2, 2);
        document.body.appendChild(canvas1);

        // Assertions
        expect(document.body.contains(canvas1)).toBe(true);
        expect(canvas1.width).toBe(4); // 2x2 blocks with scale factor of 2
        expect(canvas1.height).toBe(4);
    });

    test('Test Case 2: Larger memory section with varied colors', () => {
        const buffer2 = new ArrayBuffer(512); // 256 words
        const view2 = new DataView(buffer2);
        for (let i = 0; i < 256; i++) {
            view2.setUint16(i * 2, i); // Varying colors
        }
        const canvas2 = createMemoryVisualizer(view2, 0, 255, 16, 16, 2);
        document.body.appendChild(canvas2);

        // Assertions
        expect(document.body.contains(canvas2)).toBe(true);
        expect(canvas2.width).toBe(32); // 16x16 blocks with scale factor of 2
        expect(canvas2.height).toBe(32);
    });

    test('Test Case 3: Full memory visualization (simple)', () => {
        const buffer3 = new ArrayBuffer(65536); // 32768 words
        const view3 = new DataView(buffer3);
        for (let i = 0; i < 32768; i++) {
            view3.setUint16(i * 2, i); // Varying colors
        }
        const canvas3 = createMemoryVisualizer(view3, 0, 32767, 64, 512, 2);
        document.body.appendChild(canvas3);

        // Assertions
        expect(document.body.contains(canvas3)).toBe(true);
        expect(canvas3.width).toBe(128); // 64x512 blocks with scale factor of 2
        expect(canvas3.height).toBe(1024);
    });

    test('Test Case 4: Non-sequential memory section', () => {
        const buffer4 = new ArrayBuffer(128); // 64 words
        const view4 = new DataView(buffer4);
        view4.setUint16(0, 0b0000011111100000); // Green
        view4.setUint16(10, 0b1111100000000000); // Red
        view4.setUint16(20, 0b0000000000011111); // Blue

        const canvas4 = createMemoryVisualizer(view4, 0, 20, 8, 8, 2);
        document.body.appendChild(canvas4);

        // Assertions
        expect(document.body.contains(canvas4)).toBe(true);
        expect(canvas4.width).toBe(16); // 8x8 blocks with scale factor of 2
        expect(canvas4.height).toBe(16);
    });

    test('Test Case 5: Minimal input (single word)', () => {
        const buffer5 = new ArrayBuffer(2); // 1 word
        const view5 = new DataView(buffer5);
        view5.setUint16(0, 0b1111100000000000); // Red

        const canvas5 = createMemoryVisualizer(view5, 0, 0, 1, 1, 2);
        document.body.appendChild(canvas5);

        // Assertions
        expect(document.body.contains(canvas5)).toBe(true);
        expect(canvas5.width).toBe(2); // 1x1 block with scale factor of 2
        expect(canvas5.height).toBe(2);
    });
});