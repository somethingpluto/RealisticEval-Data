/**
 * Determine if the point (x, y) is inside the given polygon.
 * The polygon is defined as an array of tuples [x, y] representing the vertices.
 *
 * @param {Array} point - An array [x, y] representing the point to check.
 * @param {Array} polygon - An array of arrays [x, y] representing the vertices of the polygon.
 * @returns {boolean} - True if the point is inside the polygon, False otherwise.
 */
function isPointInPolygon(point, polygon) {
    const x = point[0];
    const y = point[1];
    let inside = false;
    const n = polygon.length;
    const p1x = polygon[0][0];
    const p1y = polygon[0][1];

    for (let i = 0; i < n + 1; i++) {
        const p2x = polygon[i % n][0];
        const p2y = polygon[i % n][1];
        if (y > Math.min(p1y, p2y)) {
            if (y <= Math.max(p1y, p2y)) {
                if (x <= Math.max(p1x, p2x)) {
                    if (p1y !== p2y) {
                        const xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x;
                        if (p1x === p2x || x <= xinters) {
                            inside = !inside;
                        }
                    } else if (p1x === p2x || x <= p2x) {
                        inside = !inside;
                    }
                }
            }
        }
        p1x = p2x;
        p1y = p2y;
    }

    return inside;
}