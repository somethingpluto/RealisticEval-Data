function safeSplice<T>(
    inputArray: T[],
    amountToRemove: number,
    indexToRemove: number,
    replaceWith?: T
): T[] {
    const before = inputArray.slice(0, indexToRemove);
    const after = inputArray.slice(indexToRemove + amountToRemove);

    if (replaceWith !== undefined) {
        before.push(replaceWith);
    }

    return before.concat(after);
}