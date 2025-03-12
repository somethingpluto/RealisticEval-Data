/**
 * Check if a point is inside a triangle defined by three vertices.
 *
 * @param {number} px - The x-coordinate of the point to check.
 * @param {number} py - The y-coordinate of the point to check.
 * @param {number} x1 - The x-coordinate of the first vertex of the triangle.
 * @param {number} y1 - The y-coordinate of the first vertex of the triangle.
 * @param {number} x2 - The x-coordinate of the second vertex of the triangle.
 * @param {number} y2 - The y-coordinate of the second vertex of the triangle.
 * @param {number} x3 - The x-coordinate of the third vertex of the triangle.
 * @param {number} y3 - The y-coordinate of the third vertex of the triangle.
 * @returns {boolean} True if the point (px, py) is inside or on the edge of the triangle formed by the vertices (x1, y1), (x2, y2), (x3, y3); False otherwise.
 */
function isPointInsideTriangle(px, py, x1, y1, x2, y2, x3, y3) {
    // Helper function to calculate the area of a triangle given its vertices
    function triangleArea(x1, y1, x2, y2, x3, y3) {
        return Math.abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2);
    }

    // Calculate the area of the main triangle
    const mainArea = triangleArea(x1, y1, x2, y2, x3, y3);

    // Calculate the area of the sub-triangles formed by the point and the vertices of the main triangle
    const area1 = triangleArea(px, py, x1, y1, x2, y2);
    const area2 = triangleArea(px, py, x2, y2, x3, y3);
    const area3 = triangleArea(px, py, x3, y3, x1, y1);

    // If the sum of the areas of the sub-triangles equals the area of the main triangle,
    // the point is inside or on the edge of the triangle
    return mainArea === area1 + area2 + area3;
}
describe('TestPointInsideTriangle', () => {
    it('should return true when the point is inside the triangle', () => {
        const triangleVertices = [0, 0, 5, 0, 2.5, 5];
        const point = [2.5, 2];  // Inside the triangle
        expect(isPointInsideTriangle(point[0], point[1], ...triangleVertices)).toBe(true);
    });

    it('should return true when the point is on the edge of the triangle', () => {
        const triangleVertices = [0, 0, 5, 0, 2.5, 5];
        const point = [2.5, 0];  // On the edge of the triangle
        expect(isPointInsideTriangle(point[0], point[1], ...triangleVertices)).toBe(true);
    });

    it('should return false when the point is outside the triangle', () => {
        const triangleVertices = [0, 0, 5, 0, 2.5, 5];
        const point = [6, 2];  // Outside the triangle
        expect(isPointInsideTriangle(point[0], point[1], ...triangleVertices)).toBe(false);
    });

    it('should return true when the point is at one of the triangle\'s vertices', () => {
        const triangleVertices = [0, 0, 5, 0, 2.5, 5];
        const point = [0, 0];  // At the vertex of the triangle
        expect(isPointInsideTriangle(point[0], point[1], ...triangleVertices)).toBe(true);
    });
});
