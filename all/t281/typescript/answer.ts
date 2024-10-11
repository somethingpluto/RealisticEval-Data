function squaredEuclideanDistance(vec1: number[], vec2: number[]): number {
    /**
     * Compute the squared Euclidean distance between two vectors.
     *
     * @param {number[]} vec1 - First vector.
     * @param {number[]} vec2 - Second vector.
     * @returns {number} - Euclidean distance between vec1 and vec2.
     */
    if (vec1.length !== vec2.length) {
        throw new Error("Vectors must have the same length");
    }

    let sum = 0;
    for (let i = 0; i < vec1.length; i++) {
        sum += Math.pow(vec1[i] - vec2[i], 2);
    }
    return sum;
}