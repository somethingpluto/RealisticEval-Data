function divideList(lst, n) {
    /**
     * Divide an array into n parts as evenly as possible. Excess elements are distributed to earlier subarrays.
     *
     * @param {Array} lst - The array to be divided.
     * @param {number} n - The number of parts to divide the array into.
     *
     * @returns {Array<Array>} - An array containing n subarrays, where each subarray represents a part of the original array.
     */
    // Total number of elements in the array
    const L = lst.length;
    // Calculate the size of each part
    const baseSize = Math.floor(L / n);
    // Calculate the number of sections that will have an additional element
    const remainder = L % n;

    const result = [];
    // Start index of the subarray
    let startIndex = 0;

    for (let i = 0; i < n; i++) {
        // Determine the size of the current part
        const partSize = baseSize + (i < remainder ? 1 : 0);
        // Append the subarray to the result array
        result.push(lst.slice(startIndex, startIndex + partSize));
        // Update the start index for the next part
        startIndex += partSize;
    }

    return result;
}