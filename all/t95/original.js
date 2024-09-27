//Generated by chatgpt:
// Generic function to find index values based on a comparator function
function getIndexValues(inputArray, comparatorFn) {
    let currentIndexValues = [];
    for (let i = 0; i < inputArray.length; i++) {
        if (currentIndexValues.length === 0) {
            currentIndexValues.push([i, inputArray[i]]);
        } else {
            const comparisonResult = comparatorFn(inputArray[i], currentIndexValues[0][1]);
            if (comparisonResult < 0) {
                currentIndexValues = [[i, inputArray[i]]];
            } else if (comparisonResult === 0) {
                currentIndexValues.push([i, inputArray[i]]);
            }
        }
    }
    return currentIndexValues;
}

//Generated by chatgpt:
// Comparator function for finding the minimum value
function compareMin(a, b) {
    return a - b;
}

//Generated by chatgpt:
// Comparator function for finding the maximum value
function compareMax(a, b) {
    return b - a;
}

//Generated by chatgpt:
// Specific functions for finding the minimum and maximum index values
function getMinIndex(inputArray) {
    return getIndexValues(inputArray, compareMin);
}

//Generated by chatgpt:
function getMaxIndex(inputArray) {
    return getIndexValues(inputArray, compareMax);
}