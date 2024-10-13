/**
 * Determine if the point (x, y) is inside the given polygon.
 * The polygon is defined as an array of tuples (x, y) representing the vertices.
 *
 * @param point - A tuple (x, y) representing the point to check.
 * @param polygon - An array of tuples (x, y) representing the vertices of the polygon.
 * @returns True if the point is inside the polygon, False otherwise.
 */
function isPointInPolygon(point: [number, number], polygon: [number, number][]): boolean {
    const [x, y] = point;
    let inside = false;
    const n = polygon.length;
    let [p1x, p1y] = polygon[0];

    for (let i = 0; i < n + 1; i++) {
        const [p2x, p2y] = polygon[i % n];
        if (y > Math.min(p1y, p2y)) {
            if (y <= Math.max(p1y, p2y)) {
                if (x <= Math.max(p1x, p2x)) {
                    if (p1y !== p2y) {
                        const xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x;
                        if (p1x === p2x || x <= xinters) {
                            inside = !inside;
                        }
                    } else {
                        if (p1x === p2x) {
                            inside = !inside;
                        }
                    }
                }
            }
        }
        [p1x, p1y] = [p2x, p2y];
    }

    return inside;
}