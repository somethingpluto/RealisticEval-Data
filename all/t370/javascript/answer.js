function decompose(n, shape) {
    if (typeof n !== 'number' || typeof shape !== 'object') {
        throw new Error('Invalid arguments');
    }

    let result = [];
    let totalElements = 1;

    // Calculate total number of elements in the array
    for(let i=0; i<shape.length; i++) {
        totalElements *= shape[i];
    }

    // Check if n is within valid range
    if(n < 0 || n >= totalElements) {
        throw new Error('Index out of bounds');
    }

    // Calculate multidimensional index
    for(let i=shape.length-1; i>=0; i--) {
        result.unshift(Math.floor(n / totalElements));
        n %= totalElements;
        totalElements /= shape[i];
    }

    return result;
}