function divideList(lst, n) {
    /**
     * Divide a list evenly into n parts and return a list of these parts.
     * If the list length is not divisible by n, additional elements are added to the previous sections one by one.
     *
     * @param {Array} lst - The list to be divided.
     * @param {number} n - The number of parts to divide the list into.
     * @returns {Array} - A list containing n sublists, where each sublist represents a part of the original list.
     */

    // Calculate the size of each chunk
    const chunkSize = Math.ceil(lst.length / n);
    const result = [];

    for (let i = 0; i < lst.length; i += chunkSize) {
        result.push(lst.slice(i, i + chunkSize));
    }

    return result;
}