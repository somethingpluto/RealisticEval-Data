// Function to be tested
function shuffle(array) {
    let currentIndex = array.length;

    while (currentIndex > 0) {
        const randomIndex = Math.floor(Math.random() * currentIndex);
        currentIndex--;

        // Swap the elements at currentIndex and randomIndex
        const temp = array[currentIndex];
        array[currentIndex] = array[randomIndex];
        array[randomIndex] = temp;
    }

    return array;
}

// Test cases for the shuffle function

function runShuffleTestCases() {
    // Test Case 1: Shuffle an array of numbers
    const array1 = [1, 2, 3, 4, 5];
    const shuffledArray1 = shuffle([...array1]); // Copy to avoid mutating the original array
    console.assert(
        shuffledArray1.length === array1.length && shuffledArray1.every(item => array1.includes(item)),
        "Test Case 1 Failed"
    );

    // Test Case 2: Shuffle an array of strings
    const array2 = ["a", "b", "c", "d", "e"];
    const shuffledArray2 = shuffle([...array2]);
    console.assert(
        shuffledArray2.length === array2.length && shuffledArray2.every(item => array2.includes(item)),
        "Test Case 2 Failed"
    );

    // Test Case 3: Shuffle an array with duplicate elements
    const array3 = [1, 2, 2, 3, 4];
    const shuffledArray3 = shuffle([...array3]);
    console.assert(
        shuffledArray3.length === array3.length && shuffledArray3.every(item => array3.includes(item)),
        "Test Case 3 Failed"
    );

    // Test Case 4: Shuffle an empty array
    const array4 = [];
    const shuffledArray4 = shuffle([...array4]);
    console.assert(
        shuffledArray4.length === 0,
        "Test Case 4 Failed"
    );

    // Test Case 5: Shuffle an array with one element
    const array5 = [42];
    const shuffledArray5 = shuffle([...array5]);
    console.assert(
        JSON.stringify(shuffledArray5) === JSON.stringify(array5),
        "Test Case 5 Failed"
    );

    console.log("All shuffle test cases passed!");
}

// Run all test cases
runShuffleTestCases();
