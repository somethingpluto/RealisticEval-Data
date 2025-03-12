// Start of the TypeScript file
import { RingFormat, HolePositions } from './types';

function convertToRingFormat(holes: HolePositions): RingFormat {
  if (holes.some(pos => pos < 0 || pos >= 32)) {
    throw new Error('Hole positions must be within the range of 0 to 31.');
  }
  // ... rest of the function remains unchanged
}

// ... rest of the TypeScript file
describe('TestConvertToRingFormat', () => {
    it('test_no_holes', () => {
        // Test with no holes provided.
        const holes: number[] = [];
        const expected: number[] = [1].fill(1, 0, 32);  // All positions should be 1
        const result = convertToRingFormat(holes);
        expect(result).toEqual(expected);
    });

    it('test_single_hole', () => {
        // Test with a single hole position.
        const holes: number[] = [5];
        const expected: number[] = [1].fill(1, 0, 32);
        expected[5] = 0;  // Only position 5 should be 0
        const result = convertToRingFormat(holes);
        expect(result).toEqual(expected);
    });

    it('test_multiple_holes', () => {
        // Test with multiple hole positions.
        const holes: number[] = [0, 2, 4, 8, 16];
        const expected: number[] = [1].fill(1, 0, 32);
        holes.forEach(hole => {
            expected[hole] = 0;  // Set specified positions to 0
        });
        const result = convertToRingFormat(holes);
        expect(result).toEqual(expected);
    });

    it('test_hole_out_of_bounds', () => {
        // Test with some hole positions out of bounds.
        const holes: number[] = [-1, 32, 5, 10];  // -1 and 32 are out of bounds
        const expected: number[] = [1].fill(1, 0, 32);
        expected[5] = 0;  // Only position 5 and 10 should be 0
        expected[10] = 0;
        const result = convertToRingFormat(holes);
        expect(result).toEqual(expected);
    });

    it('test_all_holes', () => {
        // Test with all positions as holes.
        const holes: number[] = Array.from({ length: 32 }, (_, i) => i);  // All positions from 0 to 31
        const expected: number[] = [0].fill(0, 0, 32);  // All positions should be 0
        const result = convertToRingFormat(holes);
        expect(result).toEqual(expected);
    });
});
