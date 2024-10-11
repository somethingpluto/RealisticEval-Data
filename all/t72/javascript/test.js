describe('get_3d_coordinates', () => {
    it('should convert 2D pixel coordinates to 3D world coordinates', () => {
        const K = [
            [500, 0, 320],
            [0, 500, 240],
            [0, 0, 1]
        ];
        const d = 10;
        const x = 320;
        const y = 240;

        const result = get_3d_coordinates(K, d, x, y);
        expect(result).toEqual([0, 0, 10]);
    });

    it('should handle different depths correctly', () => {
        const K = [
            [500, 0, 320],
            [0, 500, 240],
            [0, 0, 1]
        ];
        const d1 = 10;
        const d2 = 20;
        const x = 320;
        const y = 240;

        const result1 = get_3d_coordinates(K, d1, x, y);
        const result2 = get_3d_coordinates(K, d2, x, y);

        expect(result1).toEqual([0, 0, 10]);
        expect(result2).toEqual([0, 0, 20]);
    });
});