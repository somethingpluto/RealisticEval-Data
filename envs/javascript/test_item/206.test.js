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
    const distance = Math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2);

    // If the distance is greater than the sum of the radii, they do not intersect
    if (distance >= r1 + r2) {
        return 0;
    }

    // If one circle is inside the other, the intersection area is the area of the smaller circle
    if (distance <= Math.abs(r1 - r2)) {
        return Math.PI * Math.min(r1, r2) ** 2;
    }

    // Calculate the angles for the sector areas
    const angle1 = 2 * Math.acos((r1 ** 2 + distance ** 2 - r2 ** 2) / (2 * r1 * distance));
    const angle2 = 2 * Math.acos((r2 ** 2 + distance ** 2 - r1 ** 2) / (2 * r2 * distance));

    // Calculate the areas of the sectors
    const sectorArea1 = 0.5 * r1 ** 2 * angle1;
    const sectorArea2 = 0.5 * r2 ** 2 * angle2;

    // Calculate the areas of the triangles
    const triangleArea1 = 0.5 * r1 ** 2 * Math.sin(angle1);
    const triangleArea2 = 0.5 * r2 ** 2 * Math.sin(angle2);

    // The intersection area is the sum of the sector areas minus the sum of the triangle areas
    return sectorArea1 + sectorArea2 - triangleArea1 - triangleArea2;
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
