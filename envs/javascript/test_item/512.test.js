/**
 * Convert an array of hole positions to the ring format (array of 1s and 0s).
 *
 * @param {number[]} holes - An array of integers representing the positions of the holes (0-indexed).
 * @returns {number[]} An array of length 32, where positions with holes are 0 and others are 1.
 */
function convertToRingFormat(holes) {
    let ringFormat = new Array(32).fill(1);
    for (let i = 0; i < holes.length; i++) {
        ringFormat[holes[i]] = 0;
    }
    return ringFormat;
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
