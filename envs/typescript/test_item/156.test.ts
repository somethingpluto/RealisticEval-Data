import { formatNumber } from './formatNumber';

describe('formatNumber', () => {
  it('returns the original number if it is less than 1,000', () => {
    expect(formatNumber(999)).toBe('999');
  });

  it('returns the number formatted as "x.xK" if it is between 1,000 and 999,999', () => {
    expect(formatNumber(1234)).toBe('1.2K');
    expect(formatNumber(123456)).toBe('123.5K');
  });

  it('returns the number formatted as "x.xM" if it is one million or more', () => {
    expect(formatNumber(1000000)).toBe('1.0M');
    expect(formatNumber(1000000000)).toBe('1.0B');
  });
});
describe('formatNumber', () => {
    test('should format numbers greater than or equal to 1,000,000 with "M" suffix', () => {
        // @ts-ignore
        expect(formatNumber(1500000)).toBe('1.5M');
        // @ts-ignore
        expect(formatNumber(1000000)).toBe('1.0M');
    });

    test('should format numbers greater than or equal to 1,000 but less than 1,000,000 with "K" suffix', () => {
        // @ts-ignore
        expect(formatNumber(2500)).toBe('2.5K');
        // @ts-ignore
        expect(formatNumber(1000)).toBe('1.0K');
    });

    test('should return the number as a string if it is less than 1,000', () => {
        // @ts-ignore
        expect(formatNumber(999)).toBe('999');
        // @ts-ignore
        expect(formatNumber(500)).toBe('500');
    });


    test('should handle edge cases like exactly 1,000 or 1,000,000', () => {
        // @ts-ignore
        expect(formatNumber(1000)).toBe('1.0K');
        // @ts-ignore
        expect(formatNumber(1000000)).toBe('1.0M');
    });
});

