// Function to be tested
function adjustArrayLength(targetLength, array) {
    const arrayLength = array.length;

    if (arrayLength === 0 || targetLength === 0) {
        return [];
    }

    if (arrayLength === targetLength) {
        return array;
    }

    if (arrayLength < targetLength) {
        const repeatedArray = Array(Math.ceil(targetLength / arrayLength)).fill(array).flat();
        return repeatedArray.slice(0, targetLength);
    }

    return array.slice(0, targetLength);
}

// Test cases for the adjustArrayLength function

function runTestCases() {
    // Test Case 1: Array length equal to the target length
    const testCase1 = adjustArrayLength(5, [1, 2, 3, 4, 5]);
    console.assert(
        JSON.stringify(testCase1) === JSON.stringify([1, 2, 3, 4, 5]),
        "Test Case 1 Failed"
    );

    // Test Case 2: Array length shorter than the target length
    const testCase2 = adjustArrayLength(8, [1, 2, 3]);
    console.assert(
        JSON.stringify(testCase2) === JSON.stringify([1, 2, 3, 1, 2, 3, 1, 2]),
        "Test Case 2 Failed"
    );

    // Test Case 3: Array length longer than the target length
    const testCase3 = adjustArrayLength(3, [1, 2, 3, 4, 5]);
    console.assert(
        JSON.stringify(testCase3) === JSON.stringify([1, 2, 3]),
        "Test Case 3 Failed"
    );

    // Test Case 4: Array length shorter than the target length, target length is a multiple of array length
    const testCase4 = adjustArrayLength(6, [10, 20]);
    console.assert(
        JSON.stringify(testCase4) === JSON.stringify([10, 20, 10, 20, 10, 20]),
        "Test Case 4 Failed"
    );

    // Test Case 5: Empty array with a target length greater than zero
    const testCase5 = adjustArrayLength(4, []);
    console.assert(
        JSON.stringify(testCase5) === JSON.stringify([]),
        "Test Case 5 Failed"
    );

    console.log("All test cases passed!");
}

// Run all test cases
runTestCases();
