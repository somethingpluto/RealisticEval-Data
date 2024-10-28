describe('TestIm2Col', () => {
    it('test_single_channel_no_padding_stride_1', () => {
        const image = new Float32Array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]);
        image.shape = [1, 4, 4]; // Assuming a custom shape property for demonstration purposes
        const filterHeight = 2;
        const filterWidth = 2;
        const stride = 1;
        const padding = 0;

        const expectedOutput = [
            [1, 2, 3, 5, 6, 7, 9, 10, 11],
            [2, 3, 4, 6, 7, 8, 10, 11, 12],
            [5, 6, 7, 9, 10, 11, 13, 14, 15],
            [6, 7, 8, 10, 11, 12, 14, 15, 16]
        ];
        const output = im2col(image, filterHeight, filterWidth, stride, padding);
        expect(output).toEqual(expectedOutput);
    });

    it('test_single_channel_no_padding_stride_2', () => {
        const image = new Float32Array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]);
        image.shape = [1, 4, 4]; // Assuming a custom shape property for demonstration purposes
        const filterHeight = 2;
        const filterWidth = 2;
        const stride = 2;
        const padding = 0;

        const expectedOutput = [
            [1, 3, 9, 11],
            [2, 4, 10, 12],
            [5, 7, 13, 15],
            [6, 8, 14, 16]
        ];
        const output = im2col(image, filterHeight, filterWidth, stride, padding);
        expect(output).toEqual(expectedOutput);
    });

    it('test_multi_channel_no_padding_stride_1', () => {
        const image = new Float32Array([1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 8, 7, 6, 5, 4, 3, 2, 1]);
        image.shape = [2, 3, 3]; // Assuming a custom shape property for demonstration purposes
        const filterHeight = 2;
        const filterWidth = 2;
        const stride = 1;
        const padding = 0;

        const expectedOutput = [
            [1, 2, 4, 5],
            [2, 3, 5, 6],
            [4, 5, 7, 8],
            [5, 6, 8, 9],
            [9, 8, 6, 5],
            [8, 7, 5, 4],
            [6, 5, 3, 2],
            [5, 4, 2, 1]
        ];
        const output = im2col(image, filterHeight, filterWidth, stride, padding);
        expect(output).toEqual(expectedOutput);
    });
});