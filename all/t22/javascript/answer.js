function calculateEuclideanDistance(point1, point2) {
    /**
     * calculate the Euclidean distance between two points in a 2D space.
     *
     * @param {Array} point1 - The first point as an array of coordinates [x1, y1].
     * @param {Array} point2 - The second point as an array of coordinates [x2, y2].
     * @returns {number} The Euclidean distance between the two points.
     */

    const x1 = point1[0];
    const y1 = point1[1];
    const x2 = point2[0];
    const y2 = point2[1];

    return Math.sqrt(Math.pow(x2 - x1, 2) + Math.pow(y2 - y1, 2));
}