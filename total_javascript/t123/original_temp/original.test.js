// Function to be tested
function scaleToRange(inputArray, inputMin, inputMax, outputMin, outputMax) {
    // Ensure all values in inputArray are within the input range
    inputArray.forEach(value => {
        if (value < inputMin || value > inputMax) {
            throw new Error(`Value ${value} in inputArray is outside the range [${inputMin}, ${inputMax}].`);
        }
    });

    const scale = (outputMax - outputMin) / (inputMax - inputMin);
    
    return inputArray.map(value => ((value - inputMin) * scale) + outputMin);
}

// New test cases for the scaleToRange function

function runNewTestCases() {
    // Test Case 1: Scaling an array with a single value within the range
    const testCase1 = scaleToRange([3], 1, 5, 0, 10);
    console.assert(
        JSON.stringify(testCase1) === JSON.stringify([5]),
        "Test Case 1 Failed"
    );

    // Test Case 2: Scaling with input range and output range both being negative
    const testCase2 = scaleToRange([-10, -5, 0], -10, 0, -100, -50);
    console.assert(
        JSON.stringify(testCase2) === JSON.stringify([-100, -75, -50]),
        "Test Case 2 Failed"
    );

    // Test Case 3: Scaling an array with values already within the output range
    const testCase3 = scaleToRange([1, 2, 3], 1, 3, 1, 3);
    console.assert(
        JSON.stringify(testCase3) === JSON.stringify([1, 2, 3]),
        "Test Case 3 Failed"
    );

    // Test Case 4: Scaling with non-integer values in both input and output ranges
    const testCase4 = scaleToRange([1.5, 2.5, 3.5], 1.5, 3.5, 15, 35);
    console.assert(
        JSON.stringify(testCase4) === JSON.stringify([15, 25, 35]),
        "Test Case 4 Failed"
    );

    // Test Case 5: Scaling with all elements in the input array being the same
    const testCase5 = scaleToRange([2, 2, 2], 1, 3, 0, 100);
    console.assert(
        JSON.stringify(testCase5) === JSON.stringify([50, 50, 50]),
        "Test Case 5 Failed"
    );

    console.log("All new test cases passed!");
}

// Run all new test cases
runNewTestCases();
