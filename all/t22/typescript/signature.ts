interface Point {
    x: number;
    y: number;
}
/**
     * Calculate the Euclidean distance between two points in a 2D space.
     *
     * @param {Point} point1 - The first point as an object with x and y properties.
     * @param {Point} point2 - The second point as an object with x and y properties.
     * @returns {number} - The Euclidean distance between the two points.
*/
function calculateEuclideanDistance(point1: Point, point2: Point): number {
    
    const deltaX = point2.x - point1.x;
    const deltaY = point2.y - point1.y;
    return Math.sqrt(deltaX * deltaX + deltaY * deltaY);
}