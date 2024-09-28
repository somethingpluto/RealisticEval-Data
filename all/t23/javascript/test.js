const { getLineSegmentIntersection } = require('./path/to/your/code'); // Adjust the import based on your file structure

describe('TestLineSegmentIntersection', () => {

    test('intersecting_lines', () => {
        expect(
            getLineSegmentIntersection([[1, 1], [4, 4]], [[1, 4], [4, 1]])
        ).toEqual([2.5, 2.5]);
    });

    test('parallel_lines', () => {
        expect(
            getLineSegmentIntersection([[1, 1], [4, 4]], [[2, 2], [5, 5]])
        ).toBeNull();
    });

    test('no_intersection', () => {
        expect(
            getLineSegmentIntersection([[1, 1], [2, 2]], [[3, 3], [4, 4]])
        ).toBeNull();
    });

    test('intersection_in_middle', () => {
        const result = getLineSegmentIntersection([[0, 0], [4, 4]], [[0, 4], [4, 0]]);
        expect(result).not.toBeNull();
        expect(result[0]).toBeCloseTo(2, 7);
        expect(result[1]).toBeCloseTo(2, 7);
    });

    test('identical_segments', () => {
        expect(
            getLineSegmentIntersection([[1, 1], [4, 4]], [[1, 1], [4, 4]])
        ).toBeNull();
    });
});