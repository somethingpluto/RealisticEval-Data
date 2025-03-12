// Start of the code context
import { Point, Triangle } from './geometry';

/**
 * Checks if a point is inside a triangle defined by three vertices.
 * 
 * @param point - The point to check.
 * @param triangle - The triangle to check against.
 * @returns True if the point is inside or on the edge of the triangle; False otherwise.
 */
function isPointInsideTriangle(point: Point, triangle: Triangle): boolean {
    // Implementation remains the same
    // ...
}
// End of the code context
describe('TestPointInsideTriangle', () => {
    it('test_point_inside_triangle', () => {
        // Test case where point is inside the triangle.
        const triangleVertices = [0, 0, 5, 0, 2.5, 5];
        const point = [2.5, 2];  // Inside the triangle
        expect(isPointInsideTriangle(point[0], point[1], ...triangleVertices)).toBe(true);
    });

    it('test_point_on_edge', () => {
        // Test case where point is on the edge of the triangle.
        const triangleVertices = [0, 0, 5, 0, 2.5, 5];
        const point = [2.5, 0];  // On the edge of the triangle
        expect(isPointInsideTriangle(point[0], point[1], ...triangleVertices)).toBe(true);
    });

    it('test_point_outside_triangle', () => {
        // Test case where point is outside the triangle.
        const triangleVertices = [0, 0, 5, 0, 2.5, 5];
        const point = [6, 2];  // Outside the triangle
        expect(isPointInsideTriangle(point[0], point[1], ...triangleVertices)).toBe(false);
    });

    it('test_point_at_vertex', () => {
        // Test case where point is at one of the triangle's vertices.
        const triangleVertices = [0, 0, 5, 0, 2.5, 5];
        const point = [0, 0];  // At the vertex of the triangle
        expect(isPointInsideTriangle(point[0], point[1], ...triangleVertices)).toBe(true);
    });
});
