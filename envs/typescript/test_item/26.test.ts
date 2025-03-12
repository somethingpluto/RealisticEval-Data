// ... (previous code for context)
function convertToCommaSeparated(inputString: string): string {
  const separators = ['*', ';', '/', '-', ':'];
  const regexPattern = new RegExp(`[${separators.join('')}]`, 'g');
  return inputString.replace(regexPattern, ',');
}

// Unit tests
describe('convertToCommaSeparated', () => {
  it('should replace all specified separators with commas', () => {
    expect(convertToCommaSeparated('a*b;c/d:-e')).toBe('a,b,c,d,e');
  });

  it('should handle empty strings', () => {
    expect(convertToCommaSeparated('')).toBe('');
  });

  it('should handle strings with no separators', () => {
    expect(convertToCommaSeparated('abcdefg')).toBe('abcdefg');
  });
});
// ... (rest of the code)
describe('convertToCommaSeparated', () => {
    it('should convert basic separators', () => {
        expect(convertToCommaSeparated("apple;banana*orange/mango")).toBe("apple,banana,orange,mango");
    });

    it('should convert mixed separators in a string', () => {
        expect(convertToCommaSeparated("grapes;lemon/melon*kiwi;litchi")).toBe("grapes,lemon,melon,kiwi,litchi");
    });

    it('should convert mixed separators in another string', () => {
        expect(convertToCommaSeparated("grapes/lemon/melon*kiwi*litchi")).toBe("grapes,lemon,melon,kiwi,litchi");
    });

    it('should handle strings without separators', () => {
        expect(convertToCommaSeparated("watermelon")).toBe("watermelon");
    });
});
