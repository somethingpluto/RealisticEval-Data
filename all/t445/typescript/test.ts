import { expect } from '@jest/globals';
import * as np from 'numpy';

describe('create_rot_matrix', () => {
    it('should return a 4x4 pose matrix for X-axis rotation', () => {
        const angleDeg = 90;
        const axis = 'X';
        const result = create_rot_matrix(angleDeg, axis);

        // Assuming create_rot_matrix is defined somewhere and returns a 4x4 matrix
        expect(result).toBeInstanceOf(np.ndarray);
        expect(result.shape).toEqual([4, 4]);
    });

    it('should return a 4x4 pose matrix for Y-axis rotation', () => {
        const angleDeg = 180;
        const axis = 'Y';
        const result = create_rot_matrix(angleDeg, axis);

        expect(result).toBeInstanceOf(np.ndarray);
        expect(result.shape).toEqual([4, 4]);
    });

    it('should return a 4x4 pose matrix for Z-axis rotation', () => {
        const angleDeg = -30;
        const axis = 'Z';
        const result = create_rot_matrix(angleDeg, axis);

        expect(result).toBeInstanceOf(np.ndarray);
        expect(result.shape).toEqual([4, 4]);
    });
});