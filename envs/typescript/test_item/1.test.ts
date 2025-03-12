// Start of the code context
function numericalStrConvert(value: string): number | string {
  const trimmedValue = value.trim();
  if (trimmedValue === '') {
    return '';
  }
  // Rest of the function remains unchanged
  const parsedValue = parseFloat(trimmedValue);
  if (!isNaN(parsedValue)) {
    return parsedValue;
  }
  return parseInt(trimmedValue, 10);
}
// End of the code context
describe('TestSmartConvert', () => {
    it('should convert to integer', () => {
      expect(numericalStrConvert("123")).toBe(123);
    });
  
    it('should convert to float', () => {
      expect(numericalStrConvert("123.45")).toBe(123.45);
    });
  
    it('should remain a string for non-numeric input', () => {
      expect(numericalStrConvert("abc")).toBe("abc");
    });
  
    it('should convert to negative integer', () => {
      expect(numericalStrConvert("-456")).toBe(-456);
    });
  
    it('should convert to negative float', () => {
      expect(numericalStrConvert("-456.78")).toBe(-456.78);
    });
  });
