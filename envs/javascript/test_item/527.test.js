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
    // Calculate the area of the triangle formed by the vertices
    const area = 0.5 * (-y2 * x3 + y1 * (-x2 + x3) + x1 * (y2 - y3) + x2 * y3);

    // Calculate the areas of the triangles formed by the point and each pair of vertices
    const area1 = 0.5 * (-py * x3 + y1 * (px - x3) + x1 * (py - y3) + px * y3);
    const area2 = 0.5 * (-py * x1 + y2 * (px - x1) + x2 * (py - y1) + px * y1);
    const area3 = 0.5 * (-py * x2 + y3 * (px - x2) + x3 * (py - y2) + px * y2);

    // Check if the sum of the areas is equal to the area of the triangle
    return Math.abs(area - (area1 + area2 + area3)) < 0.000001;
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
