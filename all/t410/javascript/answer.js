function checkXorSum(combination) {
    // Ensure that combination is a typed array or a regular array and convert it to a typed array
    let arr = new Uint8Array(combination.flat());

    // Check if the length of the flattened array is divisible by 4 (assuming we're dealing with 32-bit integers)
    if(arr.length % 4 !== 0){
        throw new Error('The length of the array must be divisible by 4');
    }

    // Initialize variables to hold the xor sums
    let xor1 = 0;
    let xor2 = 0;

    // Loop through the array and calculate the xor sums
    for(let i = 0; i < arr.length; i += 4){
        xor1 ^= arr[i];
        xor2 ^= arr[i + 1];
    }

    // Check if the xor sums match the required values
    return xor1 === 0 && xor2 === 0;
}