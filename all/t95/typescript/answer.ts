function findMatchingElements<T>(arr: T[], comparisonFn: (element: T) => boolean): Array<{ element: T; index: number }> {
    const result: Array<{ element: T; index: number }> = [];

    for (let i = 0; i < arr.length; i++) {
        if (comparisonFn(arr[i])) {
            result.push({ element: arr[i], index: i });
        }
    }

    return result;
}