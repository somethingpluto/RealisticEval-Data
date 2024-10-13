function isPointOnLine(A, B, C) {
    /**
     * Check whether a point is on a line formed by two points.
     * For example, check if point C is on the line formed by points A and B.
     * 
     * @param {Array} A - point A [x, y]
     * @param {Array} B - point B [x, y]
     * @param {Array} C - point C [x, y]
     * @returns {boolean} - true if C is on the line formed by A and B, false otherwise
     */

    const [x_a, y_a] = A;
    const [x_b, y_b] = B;
    const [x_c, y_c] = C;

    // Handle the vertical line case where the x-coordinates of points A and B are the same
    if (x_a === x_b) {
        return x_c === x_a;  // C must also have the same x-coordinate
    }

    // Calculate slopes using the formula (y2 - y1) / (x2 - x1)
    // Check if slopes of AC and BC are equal
    return (y_c - y_a) * (x_b - x_a) === (y_b - y_a) * (x_c - x_a);
}