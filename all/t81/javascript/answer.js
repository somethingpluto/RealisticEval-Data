function findClosestElement(target, elements) {
    /**
     * Finds and returns the element from the given array that is closest to the specified target value.
     *
     * @param {number} target - The target number to which we want to find the closest element.
     * @param {Array<number>} elements - An array of numerical elements from which the closest element is to be found.
     * @returns {number} The element from the array that is closest to the target value.
     */

    if (!elements || elements.length === 0) {
        throw new Error("The array of elements cannot be empty.");
    }

    return elements.reduce((prev, curr) => {
        return (Math.abs(curr - target) < Math.abs(prev - target)) ? curr : prev;
    });
}
