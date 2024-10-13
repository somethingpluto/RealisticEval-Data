describe('TestLineSegmentIntersection', () => {
    it('should find the intersection at (2.5, 2.5)', () => {
        const seg1 = [[1, 1], [4, 4]];
        const seg2 = [[1, 4], [4, 1]];
        const expected = [2.5, 2.5];
        const result = getLineSegmentIntersection(seg1, seg2);
        expect(result).toEqual(expected);
    });

    it('should return null when there is no intersection', () => {
        const seg1 = [[1, 1], [2, 2]];
        const seg2 = [[3, 3], [4, 4]];
        const result = getLineSegmentIntersection(seg1, seg2);
        expect(result).toBeNull();
    });

    it('should return null for parallel segments', () => {
        const seg1 = [[1, 1], [2, 2]];
        const seg2 = [[1, 2], [2, 3]];
        const result = getLineSegmentIntersection(seg1, seg2);
        expect(result).toBeNull();
    });

    it('should return null when there is no intersection due to offset', () => {
        const seg1 = [[1, 1], [3, 3]];
        const seg2 = [[3, 2], [4, 2]];
        const result = getLineSegmentIntersection(seg1, seg2);
        expect(result).toBeNull();
    });

    it('should find the intersection at (1500.0, 1500.0) with large coordinates', () => {
        const seg1 = [[1000, 1000], [2000, 2000]];
        const seg2 = [[1000, 2000], [2000, 1000]];
        const expected = [1500.0, 1500.0];
        const result = getLineSegmentIntersection(seg1, seg2);
        expect(result).toEqual(expected);
    });
});