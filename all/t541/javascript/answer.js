/**
 * Filters elements from an array based on a qualification function.
 *
 * @param {Array} unfilteredArray - The array to filter.
 * @param {Function} isQualified - The function that determines if an element qualifies.
 * @returns {Array} - A new array containing the elements that qualify.
 */
function filterArray(unfilteredArray, isQualified) {
    const filteredResults = [];

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