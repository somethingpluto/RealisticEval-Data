/**
 * Generates integer coordinates on the line from (x1, y1) to (x2, y2) using Bresenham's line algorithm.
 *
 * Bresenham's algorithm calculates the points of an approximately straight line between two given points on a grid.
 * It is particularly well-suited for computer graphics where an efficient, integer-based algorithm is needed to
 * determine which points should be rasterized to represent the line.
 *
 * @param {number} x1 - The x-coordinate of the starting point of the line.
 * @param {number} y1 - The y-coordinate of the starting point of the line.
 * @param {number} x2 - The x-coordinate of the ending point of the line.
 * @param {number} y2 - The y-coordinate of the ending point of the line.
 * @returns {Array.<Array.<number>>} An array where each sub-array contains the x and y coordinates of a point on the line.
 */
function bresenhamLine(x1, y1, x2, y2) {
    const line = [];
    const dx = Math.abs(x2 - x1);
    const dy = Math.abs(y2 - y1);
    const sx = (x1 < x2) ? 1 : -1;
    const sy = (y1 < y2) ? 1 : -1;
    let err = dx - dy;

    while (true) {
        line.push([x1, y1]);

        if ((x1 === x2) && (y1 === y2)) break;

        const e2 = 2 * err;
        if (e2 > -dy) {
            err -= dy;
            x1 += sx;
        }
        if (e2 < dx) {
            err += dx;
            y1 += sy;
        }
    }

    return line;
}
describe('Bresenham Line Algorithm', () => {
    it('should generate horizontal line correctly', () => {
        expect(bresenhamLine(1, 5, 5, 5)).toEqual([
            [1, 5], [2, 5], [3, 5], [4, 5], [5, 5]
        ]);
    });

    it('should generate vertical line correctly', () => {
        expect(bresenhamLine(3, 2, 3, 6)).toEqual([
            [3, 2], [3, 3], [3, 4], [3, 5], [3, 6]
        ]);
    });

    it('should generate diagonal line correctly', () => {
        expect(bresenhamLine(2, 2, 6, 6)).toEqual([
            [2, 2], [3, 3], [4, 4], [5, 5], [6, 6]
        ]);
    });

    it('should generate steep slope line correctly', () => {
        expect(bresenhamLine(1, 1, 4, 6)).toEqual([
            [1, 1], [2, 2], [2, 3], [3, 4], [3, 5], [4, 6]
        ]);
    });

    it('should generate negative slope line correctly', () => {
        expect(bresenhamLine(5, 1, 1, 5)).toEqual([
            [5, 1], [4, 2], [3, 3], [2, 4], [1, 5]
        ]);
    });
});
