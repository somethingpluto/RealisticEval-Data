// ... (previous code for context)

function bresenhamLine(x1: number, y1: number, x2: number, y2: number): [number, number][] {
    const dx = Math.abs(x2 - x1);
    const dy = Math.abs(y2 - y1);
    const sx = (x1 < x2) ? 1 : -1;
    const sy = (y1 < y2) ? 1 : -1;
    let err = dx - dy;

    const points: [number, number][] = [[x1, y1]];

    while (true) {
        if (x1 === x2 && y1 === y2) break;
        const e2 = 2 * err;
        if (e2 > -dy) {
            err -= dy;
            x1 += sx;
        }
        if (e2 < dx) {
            err += dx;
            y1 += sy;
        }
        points.push([x1, y1]);
    }

    return points;
}

// ... (rest of the code)
describe('Bresenham Line Algorithm', () => {
    it('should generate horizontal line correctly', () => {
      expect(bresenhamLine(1, 5, 5, 5)).toEqual([
        [1, 5],
        [2, 5],
        [3, 5],
        [4, 5],
        [5, 5]
      ]);
    });
  
    it('should generate vertical line correctly', () => {
      expect(bresenhamLine(3, 2, 3, 6)).toEqual([
        [3, 2],
        [3, 3],
        [3, 4],
        [3, 5],
        [3, 6]
      ]);
    });
  
    it('should generate diagonal line correctly', () => {
      expect(bresenhamLine(2, 2, 6, 6)).toEqual([
        [2, 2],
        [3, 3],
        [4, 4],
        [5, 5],
        [6, 6]
      ]);
    });
  
    it('should generate steep slope correctly', () => {
      expect(bresenhamLine(1, 1, 4, 6)).toEqual([
        [1, 1],
        [2, 2],
        [2, 3],
        [3, 4],
        [3, 5],
        [4, 6]
      ]);
    });
  
    it('should generate negative slope correctly', () => {
      expect(bresenhamLine(5, 1, 1, 5)).toEqual([
        [5, 1],
        [4, 2],
        [3, 3],
        [2, 4],
        [1, 5]
      ]);
    });
  });
