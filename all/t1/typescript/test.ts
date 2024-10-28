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