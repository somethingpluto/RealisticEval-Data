function decompose(n: number, shape: number[]): [number, ...number[]] {
    let size = 1;
    for (const dim of shape) {
        size *= dim;
    }

    // Check if the index is within bounds
    if (n < 0 || n >= size) {
        throw new Error("Index out of bounds");
    }

    // Decompose the index
    const result: number[] = [];
    for (let dim of shape.slice().reverse()) {
        result.push(n % dim);
        n = Math.floor(n / dim);  // Update n by integer division
    }

    // Reverse the result to match the original shape order and return as tuple
    return result.reverse() as [number, ...number[]];
}