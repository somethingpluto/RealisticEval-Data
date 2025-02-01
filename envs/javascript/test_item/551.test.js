/**
 * Calculate the midpoints from a given array of edges.
 * For example:
 *   input: [0, 1, 2]
 *   output: [0.5, 1.5]
 *
 * @param {Array<number>} edges - An array of edge values.
 * @returns {Array<number>} An array of midpoints calculated from the edges.
 */
function getMidsFromEdges(edges) {
    if (!Array.isArray(edges) || edges.length < 2) {
        throw new Error('Input must be an array with at least two numbers.');
    }

    const midpoints = [];
    for (let i = 0; i < edges.length - 1; i++) {
        midpoints.push((edges[i] + edges[i + 1]) / 2);
    }

    return midpoints;
}
describe('TestGetMidsFromEdges', () => {
    const getMidsFromEdges = require('./getMidsFromEdges'); // Import the function to test

    describe('test_basic_case', () => {
        it('should handle a standard range of edges', () => {
            const edges = [1, 2, 3, 4];
            const expectedMids = [1.5, 2.5, 3.5];
            expect(getMidsFromEdges(edges)).toEqual(expectedMids);
        });
    });

    describe('test_single_interval', () => {
        it('should handle two edges (single interval)', () => {
            const edges = [5, 10];
            const expectedMids = [7.5];
            expect(getMidsFromEdges(edges)).toEqual(expectedMids);
        });
    });

    describe('test_multiple_intervals', () => {
        it('should handle multiple intervals', () => {
            const edges = [0, 1, 2, 3, 4, 5];
            const expectedMids = [0.5, 1.5, 2.5, 3.5, 4.5];
            expect(getMidsFromEdges(edges)).toEqual(expectedMids);
        });
    });

    describe('test_negative_edges', () => {
        it('should handle negative edges', () => {
            const edges = [-5, -3, -1, 1];
            const expectedMids = [-4.0, -2.0, 0.0];
            expect(getMidsFromEdges(edges)).toEqual(expectedMids);
        });
    });

    describe('test_zero_edges', () => {
        it('should handle edges including zero', () => {
            const edges = [0, 1, 2];
            const expectedMids = [0.5, 1.5];
            expect(getMidsFromEdges(edges)).toEqual(expectedMids);
        });
    });

    describe('test_float_edges', () => {
        it('should handle floating-point edges', () => {
            const edges = [0.0, 1.5, 3.0];
            const expectedMids = [0.75, 2.25];
            expect(getMidsFromEdges(edges)).toEqual(expectedMids);
        });
    });

    describe('test_empty_array', () => {
        it('should handle an empty array', () => {
            const edges = [];
            const expectedMids = [];
            expect(getMidsFromEdges(edges)).toEqual(expectedMids);
        });
    });
});
