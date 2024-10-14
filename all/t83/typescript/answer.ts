function rotateListElements(elements: number[]): number[] {
    /**
     * Rotate the elements of the array to the left by one position. The first element
     * is moved to the end of the array, and all other elements are shifted one position to the left.
     *
     * @param elements - An array of numbers to be rotated.
     * @returns The rotated array with elements shifted to the left by one position.
     */
    if (elements.length > 1) {
        elements = elements.slice(1).concat([elements[0]]);
    }
    return elements;
}

function rotateList<T>(elements: T[]): T[] {
    /**
     * Rotate the elements of the array, moving the first element to the end and shifting all others forward.
     *
     * @param elements - The array of elements to rotate.
     * @returns The array after rotation.
     */
    if (!elements.length) {
        return elements; // Return the array as is if it's empty
    }

    // Move the first element to the last and shift others forward
    const rotatedList = elements.slice(1).concat(elements.slice(0, 1));

    return rotatedList;
}