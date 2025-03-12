/**
 * Convert an array of hole positions to the ring format (array of 1s and 0s).
 *
 * @param {number[]} holes - An array of integers representing the positions of the holes (0-indexed).
 * @returns {number[]} An array of length 32, where positions with holes are 0 and others are 1.
 */
function convertToRingFormat(holes) {
    // Initialize an array of length 32 with all elements set to 1
    const ring = Array(32).fill(1);

    // Set the positions specified in the holes array to 0
    for (const hole of holes) {
        if (hole >= 0 && hole < 32) {
            ring[hole] = 0;
        }
    }

    return ring;
}
describe('TestConvertToRingFormat', () => {
    it('test_no_holes', () => {
        const holes = [];
        const expected = new Array(32).fill(1);  // All positions should be 1
        const result = convertToRingFormat(holes);
        expect(result).toEqual(expected);
    });

    it('test_single_hole', () => {
        const holes = [5];
        const expected = new Array(32).fill(1);
        expected[5] = 0;  // Only position 5 should be 0
        const result = convertToRingFormat(holes);
        expect(result).toEqual(expected);
    });

    it('test_multiple_holes', () => {
        const holes = [0, 2, 4, 8, 16];
        const expected = new Array(32).fill(1);
        holes.forEach(hole => {
            expected[hole] = 0;  // Set specified positions to 0
        });
        const result = convertToRingFormat(holes);
        expect(result).toEqual(expected);
    });

    it('test_hole_out_of_bounds', () => {
        const holes = [-1, 32, 5, 10];  // -1 and 32 are out of bounds
        const expected = new Array(32).fill(1);
        expected[5] = 0;  // Only position 5 and 10 should be 0
        expected[10] = 0;
        const result = convertToRingFormat(holes);
        expect(result).toEqual(expected);
    });

    it('test_all_holes', () => {
        const holes = Array.from({length: 32}, (_, i) => i);  // All positions from 0 to 31
        const expected = new Array(32).fill(0);  // All positions should be 0
        const result = convertToRingFormat(holes);
        expect(result).toEqual(expected);
    });
});
