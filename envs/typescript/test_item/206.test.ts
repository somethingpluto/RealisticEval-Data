import { Point, Circle } from './geometry';

function circleIntersectionArea(circle1: Circle, circle2: Circle): number {
  const d = distance(circle1.center, circle2.center);
  const r1 = circle1.radius;
  const r2 = circle2.radius;

  if (d >= r1 + r2) return 0;
  if (d <= Math.abs(r1 - r2)) {
    const r = r1 < r2 ? r1 : r2;
    return Math.PI * r * r;
  }

  const a1 = r1 * r1 * Math.acos((d * d + r1 * r1 - r2 * r2) / (2 * d * r1));
  const a2 = r2 * r2 * Math.acos((d * d + r2 * r2 - r1 * r1) / (2 * d * r2));
  const f = 0.5 * Math.sqrt((-d + r1 + r2) * (d + r1 - r2) * (d - r1 + r2) * (d + r1 + r2));

  return a1 + a2 - f;
}

function distance(point1: Point, point2: Point): number {
  return Math.sqrt(Math.pow(point2.x - point1.x, 2) + Math.pow(point2.y - point1.y, 2));
}
describe('Testing circleIntersectionArea function', () => {
    const tolerance = 1e-5;

    test('No overlap, circles far apart', () => {
        expect(circleIntersectionArea(0.0, 0.0, 3.0, 10.0, 10.0, 3.0)).toBeCloseTo(0.0, 5);
    });

    test('No overlap, circles just touching', () => {
        expect(circleIntersectionArea(0.0, 0.0, 3.0, 6.0, 0.0, 3.0)).toBeCloseTo(0.0, 5);
    });

    test('One circle inside the other', () => {
        const area = circleIntersectionArea(0.0, 0.0, 5.0, 2.0, 0.0, 3.0);
        expect(area).toBeCloseTo(28.2743, 5); // Area of smaller circle
    });

    test('Identical circles, full overlap', () => {
        const area = circleIntersectionArea(0.0, 0.0, 3.0, 0.0, 0.0, 3.0);
        expect(area).toBeCloseTo(28.2743, 5); // Area of one circle
    });
});
