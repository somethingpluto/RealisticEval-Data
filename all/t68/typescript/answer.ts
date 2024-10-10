type List<T> = T[];

function divideList<T>(lst: T[], n: number): List<List<T>> {
    /**
     * Divide a list evenly into n parts and return a list of these parts. If the list length is not divisible by n,
     * additional elements are added to the previous sections one by one.
     *
     * @param lst - The list to be divided.
     * @param n - The number of parts to divide the list into.
     * @returns A list containing n sublists, where each sublist represents a part of the original list.
     */
    const result: List<List<T>> = [];
    const length = lst.length;
    const size = Math.ceil(length / n);

    for (let i = 0; i < n; i++) {
        const start = i * size;
        const end = start + size;
        result.push(lst.slice(start, end));
    }

    return result;
}