describe('get3DCoordinates', () => {
    it('converts 2D pixel coordinates into 3D world coordinates correctly', () => {
        const K = np.array([
            [500, 0, 320],
            [0, 500, 240],
            [0, 0, 1]
        ]);
        const d = 10;
        const x = 320;
        const y = 240;

        const result = get3DCoordinates(K, d, x, y);

        expect(result).toEqual(np.array([0, 0, 10]));
    });

    it('handles different depth values correctly', () => {
        const K = np.array([
            [500, 0, 320],
            [0, 500, 240],
            [0, 0, 1]
        ]);
        const d = 20;
        const x = 320;
        const y = 240;

        const result = get3DCoordinates(K, d, x, y);

        expect(result).toEqual(np.array([0, 0, 20]));
    });
});