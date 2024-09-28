type Point = [number, number];
type Polygon = Point[];

function isPointInPolygon(point: Point, polygon: Polygon): boolean {
    /**
     * Determine if the point (x, y) is inside the given polygon.
     * The polygon is defined as a list of tuples (x, y) representing the vertices.
     *
     * Args:
     * point: A tuple (x, y) representing the point to check.
     * polygon: A list of tuples (x, y) representing the vertices of the polygon.
     *
     * Returns:
     * bool: True if the point is inside the polygon, False otherwise.
     */
    
    const [x, y] = point;
    let inside = false;
    const n = polygon.length;
    let [p1x, p1y] = polygon[0];

    for (let i = 0; i <= n; i++) {
        const [p2x, p2y] = polygon[i % n];
        if (y > Math.min(p1y, p2y)) {
            if (y <= Math.max(p1y, p2y)) {
                if (x <= Math.max(p1x, p2x)) {
                    if (p1y != p2y) {
                        const xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x;
                        if (p1x == p2x || x <= xinters) {
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