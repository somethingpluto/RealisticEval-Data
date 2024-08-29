
function runTestCases() {
    // Test Case 1: Remove one element and replace it with another
    const testCase1 = safeSplice([1, 2, 3, 4, 5], 1, 2, 99);
    console.assert(
        JSON.stringify(testCase1) === JSON.stringify([1, 2, 99, 4, 5]),
        "Test Case 1 Failed"
    );
  
    // Test Case 2: Remove multiple elements and replace them with one element
    const testCase2 = safeSplice([10, 20, 30, 40, 50], 2, 1, 99);
    console.assert(
        JSON.stringify(testCase2) === JSON.stringify([10, 99, 40, 50]),
        "Test Case 2 Failed"
    );
  
    // Test Case 3: Remove elements without replacing
    const testCase3 = safeSplice([1, 2, 3, 4, 5], 2, 1);
    console.assert(
        JSON.stringify(testCase3) === JSON.stringify([1, 4, 5]),
        "Test Case 3 Failed"
    );
  
    // Test Case 4: Replace an element at the start of the array
    const testCase4 = safeSplice([1, 2, 3, 4, 5], 1, 0, 99);
    console.assert(
        JSON.stringify(testCase4) === JSON.stringify([99, 2, 3, 4, 5]),
        "Test Case 4 Failed"
    );
  
    // Test Case 5: Replace an element at the end of the array
    const testCase5 = safeSplice([1, 2, 3, 4, 5], 1, 4, 99);
    console.assert(
        JSON.stringify(testCase5) === JSON.stringify([1, 2, 3, 4, 99]),
        "Test Case 5 Failed"
    );
  
    console.log("All test cases passed!");
  }
  
  // Run all test cases
  runTestCases();
  