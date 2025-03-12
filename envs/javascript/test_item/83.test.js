/**
 * Rotate the elements of the array to the left by one position. The first element
 * is moved to the end of the array, and all other elements are shifted one position to the left.
 *
 * @param {number[]} elements - An array of numbers to be rotated.
 * @returns {number[]} The rotated array with elements shifted to the left by one position.
 */
function rotateListElements(elements) {
    if (elements.length <= 1) {
        return elements;
    }
    
    const firstElement = elements.shift();
    elements.push(firstElement);
    
    return elements;
}
describe('TestRotateListElements', () => {
    it('should rotate the list elements correctly', () => {
        expect(rotateListElements([1, 2, 3, 4])).toEqual([2, 3, 4, 1]);
    });

    it('single element list should remain unchanged', () => {
        expect(rotateListElements([10])).toEqual([10]);
    });

    it('empty list should remain unchanged', () => {
        expect(rotateListElements([])).toEqual([]);
    });

    it('should correctly rotate a two-element list', () => {
        expect(rotateListElements([5, 9])).toEqual([9, 5]);
    });

    it('should correctly rotate a large list', () => {
        const largeList = Array.from({ length: 1000 }, (_, i) => i + 1);
        const rotatedList = rotateListElements(largeList);
        expect(rotatedList).toEqual(Array.from({ length: 999 }, (_, i) => i + 2).concat([1]));
    });
});
