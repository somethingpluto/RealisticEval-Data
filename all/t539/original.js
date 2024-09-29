    // Sorts an array of numbers
    sortByNumbers(arr, getField, ascending = true) {
        const sortedArr = arr.slice().sort((a, b) => {
            a = getField(a);
            b = getField(b);
            a - b
        });
        return ascending ? sortedArr : sortedArr.reverse();
    }