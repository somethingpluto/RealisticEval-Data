describe('Ray-Circle Intersection Tests', () => {
    // Test Case 1: The ray intersects the circle at two points
    test('Ray intersects circle at two points', () => {
        const ray = { origin: { x: 0, y: 0 }, direction: { x: 1, y: 1 } };
        const circle = { center: { x: 3, y: 3 }, radius: 2 };
        expect(intersects(ray, circle)).toBe(true);
    });

    // Test Case 2: The ray is tangent to the circle (one intersection point)
    test('Ray is tangent to the circle', () => {
        const ray = { origin: { x: 2, y: 0 }, direction: { x: 0, y: 1 } };
        const circle = { center: { x: 2, y: 2 }, radius: 1 };
        expect(intersects(ray, circle)).toBe(true);
    });

    // Test Case 3: The ray starts inside the circle (one intersection point)
    test('Ray starts inside the circle', () => {
        const ray = { origin: { x: 2, y: 2 }, direction: { x: 1, y: 0 } };
        const circle = { center: { x: 3, y: 2 }, radius: 1 };
        expect(intersects(ray, circle)).toBe(true);
    });

    // Test Case 4: The ray originates outside and goes away from the circle (no intersection)
    test('Ray goes away from circle (no intersection)', () => {
        const ray = { origin: { x: 5, y: 5 }, direction: { x: 1, y: 0 } };
        const circle = { center: { x: 3, y: 3 }, radius: 1 };
        expect(intersects(ray, circle)).toBe(false);
    });

    // Test Case 5: The ray is parallel to the line connecting the center of the circle and is outside (no intersection)
    test('Ray is parallel and outside circle (no intersection)', () => {
        const ray = { origin: { x: 0, y: 3 }, direction: { x: 1, y: 0 } };
        const circle = { center: { x: 3, y: 3 }, radius: 1 };
        expect(intersects(ray, circle)).toBe(true);
    });

    // Test Case 6: The ray intersects the circle at one point when passing through the center
    test('Ray passes through center of circle', () => {
        const ray = { origin: { x: 3, y: 0 }, direction: { x: 0, y: 1 } };
        const circle = { center: { x: 3, y: 3 }, radius: 3 };
        expect(intersects(ray, circle)).toBe(true);
    });
});