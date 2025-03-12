/**
 * Finds and returns the element from the given array that is closest to the specified target value.
 *
 * @param {number} target - The target number to which we want to find the closest element.
 * @param {Array<number>} elements - An array of numerical elements from which the closest element is to be found.
 * @returns {number} The element from the array that is closest to the target value.
 */
function findClosestElement(target, elements) {
    if (elements.length === 0) {
        throw new Error("The elements array must not be empty.");
    }

    let closestElement = elements[0];
    let smallestDifference = Math.abs(target - closestElement);

    for (let i = 1; i < elements.length; i++) {
        const currentElement = elements[i];
        const currentDifference = Math.abs(target - currentElement);

        if (currentDifference < smallestDifference) {
            smallestDifference = currentDifference;
            closestElement = currentElement;
        }
    }

    return closestElement;
}
describe('TestFindClosestElement', () => {
    it('should return 3 as it is the first closest element to 5', () => {
        expect(findClosestElement(5, [1, 3, 7, 8, 9])).toBe(3);
    });

    it('should return 7 as it exactly matches the target', () => {
        expect(findClosestElement(7, [1, 3, 7, 8, 9])).toBe(7);
    });

    it('should return 4 as it is the first closest element to 5', () => {
        expect(findClosestElement(5, [4, 6, 8, 9])).toBe(4);
    });

    it('should return 3.3 as it is the first closest element to 5.5', () => {
        expect(findClosestElement(5.5, [1.1, 3.3, 7.7, 8.8])).toBe(3.3);
    });
});
