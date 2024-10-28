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