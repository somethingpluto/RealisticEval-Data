function adjustArrayLength<T>(targetLength: number, array: T[]): T[] {
    const arrayLength = array.length;

    if (arrayLength === targetLength) {
        return array;
    }

    if (arrayLength < targetLength) {
        const repeatedArray = Array(Math.ceil(targetLength / arrayLength)).fill(array).flat();
        return repeatedArray.slice(0, targetLength);
    }

    return array.slice(0, targetLength);
}