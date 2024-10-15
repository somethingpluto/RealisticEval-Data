/**
 * Filters elements from an array based on a qualification function.
 *
 * @param {T[]} unfilteredArray - The array to filter.
 * @param {(element: T) => boolean} isQualified - The function that determines if an element qualifies.
 * @returns {T[]} - A new array containing the elements that qualify.
 */
function filterArray<T>(unfilteredArray: T[], isQualified: (element: T) => boolean): T[] {
    const filteredResults: T[] = [];

    // Use a for loop to iterate through each element in the unfiltered array
    for (let i = 0; i < unfilteredArray.length; i++) {
        // Check if the current element qualifies
        if (isQualified(unfilteredArray[i])) {
            // If it qualifies, push it to the results array
            filteredResults.push(unfilteredArray[i]);
        }
    }

    return filteredResults; // Return the filtered results
}