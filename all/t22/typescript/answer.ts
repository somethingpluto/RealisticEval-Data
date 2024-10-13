function calculateEuclideanDistance(point1: [number, number], point2: [number, number]): number {
    /**
     * Calculate the Euclidean distance between two points in a 2D space.
     *
     * @param point1 - The first point as a tuple of coordinates (x1, y1).
     * @param point2 - The second point as a tuple of coordinates (x2, y2).
     * @returns The Euclidean distance between the two points.
     */
    if (!Array.isArray(point1) || !Array.isArray(point2)) {
        throw new TypeError("Both points must be arrays");
    }

    if (point1.length !== 2 || point2.length !== 2) {
        throw new TypeError("Both points must be arrays of two elements");
    }

    if (!point1.every(coord => typeof coord === 'number') || !point2.every(coord => typeof coord === 'number')) {
        throw new TypeError("All coordinates must be numbers");
    }

    // Extract coordinates from the input tuples
    const [x1, y1] = point1;
    const [x2, y2] = point2;

    // Compute differences and Euclidean distance using the Pythagorean theorem
    const dx = x2 - x1;
    const dy = y2 - y1;

    return Math.sqrt(dx ** 2 + dy ** 2);
}