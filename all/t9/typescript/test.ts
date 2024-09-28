function isPointOnLine(A: number[], B: number[], C: number[]): boolean {
    const [x_a, y_a] = A;
    const [x_b, y_b] = B;
    const [x_c, y_c] = C;

    if (x_a === x_b) {
        return x_c === x_a;
    }

    return (y_c - y_a) * (x_b - x_a) === (y_b - y_a) * (x_c - x_a);
}

describe("isPointOnLine", () => {
    test("should return true when point is on the line", () => {
        const A = [0, 0];
        const B = [10, 10];
        const C = [5, 5];
        expect(isPointOnLine(A, B, C)).toBe(true);
    });

    test("should return false when point is not on the line", () => {
        const A = [0, 0];
        const B = [10, 10];
        const C = [5, 6];
        expect(isPointOnLine(A, B, C)).toBe(false);
    });

    test("should return true when point is on a vertical line", () => {
        const A = [5, 0];
        const B = [5, 10];
        const C = [5, 5];
        expect(isPointOnLine(A, B, C)).toBe(true);
    });

    test("should return true when point is on a horizontal line", () => {
        const A = [0, 5];
        const B = [10, 5];
        const C = [5, 5];
        expect(isPointOnLine(A, B, C)).toBe(true);
    });

    test("should return false when point is not on a vertical line", () => {
        const A = [5, 0];
        const B = [5, 10];
        const C = [6, 5];
        expect(isPointOnLine(A, B, C)).toBe(false);
    });
});