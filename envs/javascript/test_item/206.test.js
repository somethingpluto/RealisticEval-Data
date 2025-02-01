/**
 * Calculate the intersection area of two circles. Each circle is defined by its center coordinates and radius.
 *
 * @param {number} x1 - The x-coordinate of the center of the first circle.
 * @param {number} y1 - The y-coordinate of the center of the first circle.
 * @param {number} r1 - The radius of the first circle.
 * @param {number} x2 - The x-coordinate of the center of the second circle.
 * @param {number} y2 - The y-coordinate of the center of the second circle.
 * @param {number} r2 - The radius of the second circle.
 * @return {number} The area of the intersection between the two circles.
 */
function circleIntersectionArea(x1, y1, r1, x2, y2, r2) {
    // Calculate the distance between the centers of the two circles
    const distance = Math.sqrt(Math.pow(x2 - x1, 2) + Math.pow(y2 - y1, 2));

    // If the circles do not intersect, return 0
    if (distance >= r1 + r2) {
        return 0;
    }

    // If one circle is completely inside the other, return the area of the smaller circle
    if (distance <= Math.abs(r1 - r2)) {
        return Math.pow(Math.min(r1, r2), 2) * Math.PI;
    }

    // Calculate the intersection area using the formula
    const a = r1 * r1 * Math.acos((distance * distance + r1 * r1 - r2 * r2) / (2 * distance * r1 * r1));
    const b = r2 * r2 * Math.acos((distance * distance + r2 * r2 - r1 * r1) / (2 * distance * r2 * r2));
    const c = 0.5 * Math.sqrt((-distance + r1 + r2) * (distance + r1 - r2) * (distance - r1 + r2) * (distance + r1 + r2));

    return a + b - c;
}
describe("Testing circleIntersectionArea function", () => {
    const tolerance = 1e-5;

    test("No overlap, circles far apart", () => {
        expect(circleIntersectionArea(0.0, 0.0, 3.0, 10.0, 10.0, 3.0)).toBeCloseTo(0.0, tolerance);
    });

    test("No overlap, circles just touching", () => {
        expect(circleIntersectionArea(0.0, 0.0, 3.0, 6.0, 0.0, 3.0)).toBeCloseTo(0.0, tolerance);
    });

    test("One circle inside the other", () => {
        const area = circleIntersectionArea(0.0, 0.0, 5.0, 2.0, 0.0, 3.0);
        expect(area).toBeCloseTo(28.2743, tolerance); // Area of smaller circle
    });

    test("Identical circles, full overlap", () => {
        const area = circleIntersectionArea(0.0, 0.0, 3.0, 0.0, 0.0, 3.0);
        expect(area).toBeCloseTo(28.2743, tolerance); // Area of one circle
    });
});
