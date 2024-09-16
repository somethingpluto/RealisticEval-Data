// Sorts an array of objects with timestamps
function sortByTimestamp(arr, getField, ascending = true) {
    const sortedArr = arr.slice().sort((a, b) => {
        a = getField(a);
        b = getField(b);

        const timestampA = new Date(a).getTime();
        const timestampB = new Date(b).getTime();
        return timestampA - timestampB;
    });
    return ascending ? sortedArr : sortedArr.reverse();
}