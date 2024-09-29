
// Sorts an array of strings alphabetically
sortAlphabetically(arr, getField, ascending = true) {
    const sortedArr = arr.slice().sort((a, b) => {
        a = getField(a);
        b = getField(b);

        if (a.toLowerCase() < b.toLowerCase()) {
            return -1;
        }
        if (a.toLowerCase() > b.toLowerCase()) {
            return 1;
        }
        return 0;
    });

    return ascending ? sortedArr : sortedArr.reverse();
}