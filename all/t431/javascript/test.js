describe('intersectHorizontally', () => {
    it('test with overlapping rectangles', () => {
        const rect1 = [0, 0, 2, 2];
        const rect2 = [1, 1, 3, 3];
        expect(intersectHorizontally(rect1, rect2)).toBe(true);
    });

    it('test with rectangles touching at a point (not overlapping)', () => {
        const rect1 = [0, 0, 1, 1];
        const rect2 = [1, 1, 2, 2];
        expect(intersectHorizontally(rect1, rect2)).toBe(true);
    });

    it('test with adjacent rectangles (no overlap)', () => {
        const rect1 = [0, 0, 2, 2];
        const rect2 = [2, 0, 3, 3];
        expect(intersectHorizontally(rect1, rect2)).toBe(true);
    });

    it('test with one rectangle fully inside another', () => {
        const rect1 = [1, 1, 4, 4];
        const rect2 = [2, 2, 3, 3];
        expect(intersectHorizontally(rect1, rect2)).toBe(true);
    });

    it('test with overlapping rectangles', () => {
        const rect1 = [-1, -1, 1, 1];
        const rect2 = [0, 0, 2, 2];
        expect(intersectHorizontally(rect1, rect2)).toBe(true);
    });
});