function bresenhamLine(x1: number, y1: number, x2: number, y2: number): [number, number][] {
    let points: [number, number][] = [];
    let dx = Math.abs(x2 - x1);
    let dy = -Math.abs(y2 - y1);
    let sx = x1 < x2 ? 1 : -1;
    let sy = y1 < y2 ? 1 : -1;
    let err = dx + dy; // error value e_xy

    while (true) {
        points.push([x1, y1]);
        if (x1 === x2 && y1 === y2) {
            break;
        }
        let e2 = 2 * err;
        if (e2 >= dy) { // e_xy+e_x > 0
            err += dy;
            x1 += sx;
        }
        if (e2 <= dx) { // e_xy+e_y < 0
            err += dx;
            y1 += sy;
        }
    }

    return points;
}