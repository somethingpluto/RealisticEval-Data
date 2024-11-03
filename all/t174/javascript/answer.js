function findTForX(targetX, p0, p1, p2) {
    let t0 = 0.0;
    let t1 = 1.0;
    const tolerance = 1e-6;
    const maxIterations = 100;

    let x0 = bezierCurve(t0, p0, p1, p2) - targetX;
    let x1 = bezierCurve(t1, p0, p1, p2) - targetX;

    for (let i = 0; i < maxIterations; i++) {
        if (Math.abs(x1 - x0) < tolerance) break;

        let t2 = t1 - x1 * (t1 - t0) / (x1 - x0);
        let x2 = bezierCurve(t2, p0, p1, p2) - targetX;

        if (Math.abs(x2) < tolerance) return t2;

        t0 = t1; x0 = x1; t1 = t2; x1 = x2;
    }

    return t1; // Return the best approximation found
}

function bezierCurve(t, p0, p1, p2) {
    const oneMinusT = 1 - t;
    return (oneMinusT ** 2) * p0 + (2 * oneMinusT * t) * p1 + (t ** 2) * p2;
}