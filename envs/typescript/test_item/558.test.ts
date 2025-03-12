// degreesToRadians.ts
export function degreesToRadians(degrees: number): number {
  return degrees * (Math.PI / 180);
}

// degreesToRadians.d.ts
export declare function degreesToRadians(degrees: number): number;
describe('degreesToRadians', () => {
    it('should convert 0 degrees to 0 radians', () => {
        expect(degreesToRadians(0)).toBeCloseTo(0, 5);
    });

    it('should convert 90 degrees to π/2 radians', () => {
        expect(degreesToRadians(90)).toBeCloseTo(PI / 2, 5);
    });

    it('should convert 180 degrees to π radians', () => {
        expect(degreesToRadians(180)).toBeCloseTo(PI, 5);
    });

    it('should convert 270 degrees to 3π/2 radians', () => {
        expect(degreesToRadians(270)).toBeCloseTo(3 * PI / 2, 5);
    });

    it('should convert 360 degrees to 2π radians', () => {
        expect(degreesToRadians(360)).toBeCloseTo(2 * PI, 5);
    });

    it('should convert -90 degrees to -π/2 radians', () => {
        expect(degreesToRadians(-90)).toBeCloseTo(-PI / 2, 5);
    });

    it('should convert 720 degrees to 4π radians', () => {
        expect(degreesToRadians(720)).toBeCloseTo(4 * PI, 5);
    });
});
