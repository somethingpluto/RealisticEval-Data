const math = require('mathjs');

function createRotMatrix(angleDeg, axis) {
    let angleRad = math.rad(angleDeg);
    let cosAngle = math.cos(angleRad);
    let sinAngle = math.sin(angleRad);

    if (axis === 'X') {
        return math.matrix([
            [1, 0, 0],
            [0, cosAngle, -sinAngle],
            [0, sinAngle, cosAngle]
        ]);
    } else if (axis === 'Y') {
        return math.matrix([
            [cosAngle, 0, sinAngle],
            [0, 1, 0],
            [-sinAngle, 0, cosAngle]
        ]);
    } else if (axis === 'Z') {
        return math.matrix([
            [cosAngle, -sinAngle, 0],
            [sinAngle, cosAngle, 0],
            [0, 0, 1]
        ]);
    } else {
        throw new Error("Invalid axis provided. Must be 'X', 'Y' or 'Z'.");
    }
}