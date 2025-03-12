// ... (previous code for context)
import { Matrix } from 'mathjs';

function createRotMatrix(angleDeg: number, axis: 'X' | 'Y' | 'Z'): Matrix {
    const angleRad = angleDeg * (Math.PI / 180);
    let c = Math.cos(angleRad);
    let s = Math.sin(angleRad);
    let t = 1 - c;

    switch (axis) {
        case 'X':
            return Matrix([
                [1, 0, 0, 0],
                [0, t, -s, 0],
                [0, s, t, 0],
                [0, 0, 0, 1],
            ]);
        case 'Y':
            return Matrix([
                [c, 0, s, 0],
                [0, 1, 0, 0],
                [-s, 0, c, 0],
                [0, 0, 0, 1],
            ]);
        case 'Z':
            return Matrix([
                [c, -s, 0, 0],
                [s, c, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1],
            ]);
        default:
            throw new Error('Invalid axis');
    }
}
// ... (rest of the code)
import * as math from 'mathjs';

describe('TestCreateRotMatrix', () => {
  it('test_rotation_x_90_degrees', () => {
    /** Test rotation around X-axis for 90 degrees */
    const expectedMatrix = [
      [1, 0, 0, 0],
      [0, 0, -1, 0],
      [0, 1, 0, 0],
      [0, 0, 0, 1]
    ];
    const resultMatrix = createRotMatrix(90, 'X');
    expect(resultMatrix).toEqual(expectedMatrix);
  });

  it('test_rotation_y_180_degrees', () => {
    /** Test rotation around Y-axis for 180 degrees */
    const expectedMatrix = [
      [-1, 0, 0, 0],
      [0, 1, 0, 0],
      [0, 0, -1, 0],
      [0, 0, 0, 1]
    ];
    const resultMatrix = createRotMatrix(180, 'Y');
    expect(resultMatrix).toEqual(expectedMatrix);
  });

  it('test_rotation_z_270_degrees', () => {
    /** Test rotation around Z-axis for 270 degrees (or -90 degrees) */
    const expectedMatrix = [
      [0, 1, 0, 0],
      [-1, 0, 0, 0],
      [0, 0, 1, 0],
      [0, 0, 0, 1]
    ];
    const resultMatrix = createRotMatrix(270, 'Z');
    expect(resultMatrix).toEqual(expectedMatrix);
  });

  it('test_invalid_axis', () => {
    /** Test behavior with invalid axis input */
    expect(() => createRotMatrix(90, 'A')).toThrow('Invalid axis. Must be one of \'X\', \'Y\', or \'Z\'.');
  });

  it('test_zero_rotation', () => {
    /** Test zero degree rotation which should lead to identity matrix */
    const expectedMatrix = [
      [1, 0, 0, 0],
      [0, 1, 0, 0],
      [0, 0, 1, 0],
      [0, 0, 0, 1]
    ];
    const resultMatrix = createRotMatrix(0, 'X');
    expect(resultMatrix).toEqual(expectedMatrix);
  });
});
