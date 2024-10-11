function bresenhamLine(x1: number, y1: number, x2: number, y2: number): [number, number][] {
    const result: [number, number][] = [];

    let dx = Math.abs(x2 - x1);
    let dy = Math.abs(y2 - y1);
    let sx = (x1 < x2) ? 1 : -1;
    let sy = (y1 < y2) ? 1 : -1;
    let err = dx - dy;

    while(true) {
        result.push([x1, y1]);

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

    return result;
}