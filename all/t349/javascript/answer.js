/**
 * Generates all possible combinations of elements from a list of lists.
 *
 * @param {Array<Array<any>>} inputLists - A list of lists containing the elements to combine.
 *                                          The lists must not be empty but can contain elements of any type.
 * @returns {Array<Array<any>>} - A list of lists, where each inner list represents a possible combination of elements
 *                                 taken from the input lists. Returns an empty list if the input list is empty
 *                                 or if any of the input lists is empty.
 */
function generateCombinations(inputLists) {
    if (inputLists.length === 0 || inputLists.some(list => list.length === 0)) {
        return []; // Return empty if input is empty or contains any empty list
    }

    const result = [];

    function backtrack(currentCombo, index) {
        // If the current combination is the same length as inputLists, push it to the result
        if (currentCombo.length === inputLists.length) {
            result.push([...currentCombo]);
            return;
        }

        // Iterate through the elements of the current list
        for (const element of inputLists[index]) {
            currentCombo.push(element); // Add the current element to the combination
            backtrack(currentCombo, index + 1); // Move to the next list
            currentCombo.pop(); // Remove the last element for backtracking
        }
    }

    backtrack([], 0); // Start backtracking with an empty combination
    return result;
}
