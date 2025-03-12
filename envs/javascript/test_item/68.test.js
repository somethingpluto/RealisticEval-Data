/**
 * Divide an array evenly into n parts and return an array of these parts. If the array length is not divisible by n,
 * additional elements are added to the previous sections one by one.
 * 
 * @param {Array} lst - The array to be divided.
 * @param {number} n - The number of parts to divide the array into.
 * 
 * @returns {Array<Array>} - An array containing n subarrays, where each subarray represents a part of the original array.
 */
function divideList(lst, n) {
    const result = [];
    const len = lst.length;
    const baseSize = Math.floor(len / n);
    const extra = len % n;
    let start = 0;

    for (let i = 0; i < n; i++) {
        const size = baseSize + (i < extra ? 1 : 0);
        result.push(lst.slice(start, start + size));
        start += size;
    }

    return result;
}
describe('TestDivideList', () => {
    it('should handle even division', () => {
        const lst = [1, 2, 3, 4, 5, 6];
        const n = 3;
        const expected = [[1, 2], [3, 4], [5, 6]];
        expect(divideList(lst, n)).toEqual(expected);
    });

    it('should handle uneven division', () => {
        const lst = [1, 2, 3, 4, 5, 6, 7];
        const n = 3;
        const expected = [[1, 2, 3], [4, 5], [6, 7]];
        expect(divideList(lst, n)).toEqual(expected);
    });

    it('should handle more parts than items', () => {
        const lst = [1, 2, 3];
        const n = 5;
        const expected = [[1], [2], [3], [], []];
        expect(divideList(lst, n)).toEqual(expected);
    });

    it('should handle a single element', () => {
        const lst = [1];
        const n = 1;
        const expected = [[1]];
        expect(divideList(lst, n)).toEqual(expected);
    });

    it('should handle an empty list', () => {
        const lst = [];
        const n = 3;
        const expected = [[], [], []];
        expect(divideList(lst, n)).toEqual(expected);
    });
});
