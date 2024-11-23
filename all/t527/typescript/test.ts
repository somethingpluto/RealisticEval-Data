describe('TestPointInsideTriangle', () => {
    it('test_point_inside_triangle', () => {
        // Test case where point is inside the triangle.
        const triangleVertices = [0, 0, 5, 0, 2.5, 5];
        const point = [2.5, 2];  // Inside the triangle
        const [x1, y1, x2, y2, x3, y3] = triangleVertices;
        expect(isPointInsideTriangle(point[0], point[1], x1, y1, x2, y2, x3, y3)).toBe(true);
    });

    it('test_point_on_edge', () => {
        // Test case where point is on the edge of the triangle.
        const triangleVertices = [0, 0, 5, 0, 2.5, 5];
        const point = [2.5, 0];  // On the edge of the triangle
        const [x1, y1, x2, y2, x3, y3] = triangleVertices;
        expect(isPointInsideTriangle(point[0], point[1], x1, y1, x2, y2, x3, y3)).toBe(true);
    });

    it('test_point_outside_triangle', () => {
        // Test case where point is outside the triangle.
        const triangleVertices = [0, 0, 5, 0, 2.5, 5];
        const point = [6, 2];  // Outside the triangle
        const [x1, y1, x2, y2, x3, y3] = triangleVertices;
        expect(isPointInsideTriangle(point[0], point[1], x1, y1, x2, y2, x3, y3)).toBe(false);
    });

    it('test_point_at_vertex', () => {
        // Test case where point is at one of the triangle's vertices.
        const triangleVertices = [0, 0, 5, 0, 2.5, 5];
        const point = [0, 0];  // At the vertex of the triangle
        const [x1, y1, x2, y2, x3, y3] = triangleVertices;
        expect(isPointInsideTriangle(point[0], point[1], x1, y1, x2, y2, x3, y3)).toBe(true);
    });
});
