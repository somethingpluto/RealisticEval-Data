// Start of the code context
import { isCompliantFourDigit } from './complianceChecker';

// Unit tests for isCompliantFourDigit function
describe('isCompliantFourDigit', () => {
  it('should return true for a four-digit number within the range', () => {
    expect(isCompliantFourDigit(1234)).toBe(true);
    expect(isCompliantFourDigit(1000)).toBe(true);
    expect(isCompliantFourDigit(9999)).toBe(true);
  });

  it('should return false for numbers outside the four-digit range', () => {
    expect(isCompliantFourDigit(999)).toBe(false);
    expect(isCompliantFourDigit(10000)).toBe(false);
    expect(isCompliantFourDigit(-1)).toBe(false);
  });

  it('should return false for non-numeric inputs', () => {
    expect(isCompliantFourDigit('1234' as any)).toBe(false);
    expect(isCompliantFourDigit(null)).toBe(false);
    expect(isCompliantFourDigit(undefined)).toBe(false);
  });
});
// End of the code context
describe('isCompliantFourDigit', () => {
    it('should return true for a standard positive four-digit number', () => {
        expect(isCompliantFourDigit(1234)).toBe(true);
    });

    it('should return true for boundary values of the range', () => {
        expect(isCompliantFourDigit(1000)).toBe(true);
        expect(isCompliantFourDigit(9999)).toBe(true);
    });

    it('should return false for a negative four-digit number', () => {
        expect(isCompliantFourDigit(-1234)).toBe(false);
    });

    it('should return false for numbers that are out of the four-digit range', () => {
        expect(isCompliantFourDigit(999)).toBe(false);
        expect(isCompliantFourDigit(10000)).toBe(false);
    });
});
