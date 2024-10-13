function divideList(lst: number[], n: number): number[][] {
    // Total number of elements in the list
    const L = lst.length;
    // Calculate the size of each part
    const baseSize = Math.floor(L / n);
    // Calculate the number of sections that will have an additional element
    const remainder = L % n;

    const result: number[][] = [];
    // Start index of the sublist
    let startIndex = 0;

    for (let i = 0; i < n; i++) {
        // Determine the size of the current part
        const partSize = baseSize + (i < remainder ? 1 : 0);
        // Append the sublist to the result list
        result.push(lst.slice(startIndex, startIndex + partSize));
        // Update the start index for the next part
        startIndex += partSize;
    }

    return result;
}