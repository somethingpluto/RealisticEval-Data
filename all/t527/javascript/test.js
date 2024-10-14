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