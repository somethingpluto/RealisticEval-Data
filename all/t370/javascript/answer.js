function decompose(n, shape) {
    // Calculate the total size of the array
    let size = 1;
    for (let dim of shape) {
        size *= dim;
    }

    // Check if the index is within bounds
    if (!(0 <= n && n < size)) {
        throw new Error("Index out of bounds");
    }

    // Decompose the index
    let result = [];
    for (let dim of shape.slice().reverse()) {
        result.push(n % dim);
        n = Math.floor(n / dim);  // Update n by integer division
    }

    // Reverse the result to match the original shape order and return as an array
    return result.reverse();
}