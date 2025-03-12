// Additions at the start of the file
import { canCompleteCircuit } from './canCompleteCircuit';

// Unit tests for the canCompleteCircuit function
describe('canCompleteCircuit', () => {
  test('returns the correct starting index when a valid circuit exists', () => {
    expect(canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2])).toBe(3);
  });

  test('returns -1 when no valid circuit exists', () => {
    expect(canCompleteCircuit([2, 3, 4], [3, 4, 3])).toBe(-1);
  });

  test('handles empty arrays', () => {
    expect(canCompleteCircuit([], [])).toBe(-1);
  });

  test('handles arrays with one element', () => {
    expect(canCompleteCircuit([1], [1])).toBe(0);
  });

  // Add more tests as needed
});
describe('canCompleteCircuit', () => {
    it('should return the correct starting index for a single station', () => {
        const gas = [5];
        const cost = [4];
        const expected = 0;
        expect(canCompleteCircuit(gas, cost)).toBe(expected);
    });

    it('should return -1 for an impossible single station', () => {
        const gas = [4];
        const cost = [5];
        const expected = -1;
        expect(canCompleteCircuit(gas, cost)).toBe(expected);
    });

    it('should return the correct starting index for two stations', () => {
        const gas = [1, 2];
        const cost = [2, 1];
        const expected = 1;
        expect(canCompleteCircuit(gas, cost)).toBe(expected);
    });

    it('should return the correct starting index for a circular route', () => {
        const gas = [1, 2, 3, 4, 5];
        const cost = [3, 4, 5, 1, 2];
        const expected = 3;
        expect(canCompleteCircuit(gas, cost)).toBe(expected);
    });

    it('should return -1 for an impossible circular route', () => {
        const gas = [2, 3, 4];
        const cost = [3, 4, 3];
        const expected = -1;
        expect(canCompleteCircuit(gas, cost)).toBe(expected);
    });
});
