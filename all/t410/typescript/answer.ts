function checkXorSum(combination: number[][]): boolean {
    // Initialize an empty array for storing XOR results
    let xorResults: number[] = [];

    // Loop through each row of the combination matrix
    for(let i = 0; i < combination.length; i++) {
        // For each row, loop through each column and perform XOR operation
        for(let j = 0; j < combination[i].length; j++) {
            // If it's the first row, simply add the value to the result array
            if(i === 0) {
                xorResults.push(combination[i][j]);
            } else {
                // For subsequent rows, perform XOR operation with the previous result
                xorResults[j] ^= combination[i][j];
            }
        }
    }

    // Check if all XOR results are zero
    return xorResults.every(result => result === 0);
}