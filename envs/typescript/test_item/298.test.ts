// ... (previous code for context)

function setEurValue(value: string | number): string {
  if (typeof value === 'string') {
    value = parseFloat(value);
    if (isNaN(value)) return '';
  }
  if (typeof value !== 'number' || value < 0) return '';

  const suffixes = ['', 'k', 'm', 'b', 't'];
  const index = Math.floor(Math.log10(Math.abs(value)) / 3);
  const scaledValue = value / Math.pow(1000, index);

  return scaledValue.toFixed(2) + suffixes[index];
}

// ... (rest of the code)
describe('setEurValue', () => {
    test('formats standard values correctly', () => {
        expect(setEurValue('250')).toBe('250');
        expect(setEurValue('2500')).toBe('2.5k');
    });

    test('handles boundary values accurately', () => {
        expect(setEurValue('999')).toBe('999');
        expect(setEurValue('1000')).toBe('1.0k');
        expect(setEurValue('999999')).toBe('999.9k'); // Corrected from '1000.0k'
        expect(setEurValue('1000000')).toBe('1.0m');
    });

    test('returns correct format for zero and negative inputs', () => {
        expect(setEurValue('0')).toBe('0');
        expect(setEurValue('-100')).toBe('-100'); // Handling negative inputs if needed
    });

    test('returns an empty string for invalid inputs', () => {
        expect(setEurValue('hello')).toBe('');
        expect(setEurValue(null)).toBe('');
        expect(setEurValue(undefined)).toBe('');
    });

    test('ensures precision for large numbers', () => {
        expect(setEurValue('10000000')).toBe('10.0m');
        expect(setEurValue('987654321')).toBe('987.7m');
    });
});
