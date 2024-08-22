/**
 * Sorts an array of objects based on timestamp values extracted by a getter function.
 * @param {Object[]} arr - The array of objects to sort.
 * @param {function} getField - A function that takes an object and returns its timestamp.
 * @param {boolean} ascending - True for ascending order, false for descending. Defaults to true.
 * @returns {Object[]} The sorted array.
 */
function sortByTimestamp(arr, getField, ascending = true) {
    if (!Array.isArray(arr)) {
        throw new Error("The first argument must be an array.");
    }

    const sortedArr = arr.slice().sort((a, b) => {
        // Extract timestamps using the getField callback
        const dateA = new Date(getField(a));
        const dateB = new Date(getField(b));

        // Compare the timestamp values
        const timeA = dateA.getTime();
        const timeB = dateB.getTime();

        // Handle potentially invalid dates by treating them as less than valid dates
        if (isNaN(timeA)) return 1; // Push invalid dates to the end
        if (isNaN(timeB)) return -1; // Push invalid dates to the end

        // Determine sort order based on the 'ascending' flag
        return ascending ? timeA - timeB : timeB - timeA;
    });

    return sortedArr;
}