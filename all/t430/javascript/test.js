describe('intersectVertically', () => {
    it('should return true for overlapping rectangles', () => {
        const rect1 = [0, 0, 2, 2];
        const rect2 = [1, 1, 3, 3];
        expect(intersectVertically(rect1, rect2)).toBe(true);
    });

    it('should return true for overlapping rectangles', () => {
        const rect1 = [-1, -1, 1, 1];
        const rect2 = [0, 0, 2, 2];
        expect(intersectVertically(rect1, rect2)).toBe(true);
    });

    it('should return true for partially overlapping rectangles vertically', () => {
        const rect1 = [0, 1, 2, 4];
        const rect2 = [1, 0, 3, 2];
        expect(intersectVertically(rect1, rect2)).toBe(true);
    });

    it('should return true for identical rectangles', () => {
        const rect1 = [0, 0, 2, 2];
        const rect2 = [0, 0, 2, 2];
        expect(intersectVertically(rect1, rect2)).toBe(true);
    });

    it('should return true when one rectangle is completely inside the other', () => {
        const rect1 = [0, 0, 4, 4];
        const rect2 = [1, 1, 2, 2];
        expect(intersectVertically(rect1, rect2)).toBe(true);
    });
});