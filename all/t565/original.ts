function getBezierPoint(t: number, points: Coordinates[]): Coordinates {
    if (points.length === 1) {
      return points[0];
    }
  
    const nextPoints: Coordinates[] = [];
    for (let i = 0; i < points.length - 1; i++) {
      const x = (1 - t) * points[i].x + t * points[i + 1].x;
      const y = (1 - t) * points[i].y + t * points[i + 1].y;
      nextPoints.push({ x, y });
    }
  
    return getBezierPoint(t, nextPoints);
  }