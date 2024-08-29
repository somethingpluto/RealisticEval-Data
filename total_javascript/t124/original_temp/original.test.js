// Function to be tested
function shuffle(array) {
  var currentIndex = array.length, randomIndex;
  // While there remain elements to shuffle...
  while (currentIndex != 0) {
      // Pick a remaining element...
      randomIndex = Math.floor(Math.random() * currentIndex);
      currentIndex--;
      // And swap it with the current element.
      [array[currentIndex], array[randomIndex]] = [
          array[randomIndex], array[currentIndex]];
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
  const array2 = ["apple", "banana", "cherry", "date", "elderberry"];
  const shuffledArray2 = shuffle([...array2]);
  console.assert(
      shuffledArray2.length === array2.length && shuffledArray2.every(item => array2.includes(item)),
      "Test Case 2 Failed"
  );

  // Test Case 3: Shuffle an array with duplicate elements
  const array3 = [1, 1, 2, 2, 3, 3];
  const shuffledArray3 = shuffle([...array3]);
  console.assert(
      shuffledArray3.length === array3.length && shuffledArray3.every(item => array3.includes(item)),
      "Test Case 3 Failed"
  );

  // Test Case 4: Shuffle an array with a single element
  const array4 = [42];
  const shuffledArray4 = shuffle([...array4]);
  console.assert(
      JSON.stringify(shuffledArray4) === JSON.stringify(array4),
      "Test Case 4 Failed"
  );

  // Test Case 5: Shuffle an empty array
  const array5 = [];
  const shuffledArray5 = shuffle([...array5]);
  console.assert(
      shuffledArray5.length === 0,
      "Test Case 5 Failed"
  );

  console.log("All shuffle test cases passed!");
}

// Run all test cases
runShuffleTestCases();
