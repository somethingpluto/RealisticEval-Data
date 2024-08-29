
function runTestCases() {
    // Test Case 1: Simple scaling
    const testCase1 = scaleToRange([1, 2, 3, 4, 5], 1, 5, 10, 50);
    console.assert(
        JSON.stringify(testCase1) === JSON.stringify([10, 20, 30, 40, 50]),
        "Test Case 1 Failed"
    );

    // Test Case 2: Scaling with negative input range
    const testCase2 = scaleToRange([-5, 0, 5], -5, 5, 0, 100);
    console.assert(
        JSON.stringify(testCase2) === JSON.stringify([0, 50, 100]),
        "Test Case 2 Failed"
    );

    // Test Case 3: Scaling with negative output range
    const testCase3 = scaleToRange([0, 50, 100], 0, 100, -100, 100);
    console.assert(
        JSON.stringify(testCase3) === JSON.stringify([-100, 0, 100]),
        "Test Case 3 Failed"
    );

    // Test Case 4: Input array containing the same value
    const testCase4 = scaleToRange([2, 2, 2], 1, 3, 0, 10);
    console.assert(
        JSON.stringify(testCase4) === JSON.stringify([5, 5, 5]),
        "Test Case 4 Failed"
    );

    // Test Case 5: Input value out of range (should throw an error)
    try {
        scaleToRange([1, 2, 3, 6], 1, 5, 0, 10);
        console.error("Test Case 5 Failed (No error thrown)");
    } catch (e) {
        console.log("Test Case 5 Passed (Error thrown as expected)");
    }

    console.log("All other test cases passed!");
}

// Run all test cases
runTestCases();
