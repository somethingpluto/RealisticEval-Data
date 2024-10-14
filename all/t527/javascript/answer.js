function area(x1, y1, x2, y2, x3, y3) {
    // Calculate the area of a triangle given by its vertices.
    return Math.abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0);
}

function isPointInsideTriangle(px, py, x1, y1, x2, y2, x3, y3) {
    // Calculate the area of the triangle ABC
    const A = area(x1, y1, x2, y2, x3, y3);

    // Calculate the area of the triangles PAB, PBC, and PCA
    const A1 = area(px, py, x1, y1, x2, y2);
    const A2 = area(px, py, x2, y2, x3, y3);
    const A3 = area(px, py, x3, y3, x1, y1);

    // Check if the sum of A1, A2, and A3 is equal to A
    return A === (A1 + A2 + A3);
}