describe('alignLinesLeft', () => {
    it('should align equal length strings correctly', () => {
      const str1 = "Hello";
      const str2 = "World";
      const expectedStr1 = "Hello";
      const expectedStr2 = "World";
      const [alignedStr1, alignedStr2] = alignLinesLeft(str1, str2);
      expect(alignedStr1).toBe(expectedStr1);
      expect(alignedStr2).toBe(expectedStr2);
    });
  
    it('should align when the first string is longer', () => {
      const str1 = "Hello, World!";
      const str2 = "Hi";
      const expectedStr1 = "Hello, World!";
      const expectedStr2 = "Hi           "; // 14 spaces after "Hi"
      const [alignedStr1, alignedStr2] = alignLinesLeft(str1, str2);
      expect(alignedStr1).toBe(expectedStr1);
      expect(alignedStr2).toBe(expectedStr2);
    });
  
    it('should align when the second string is longer', () => {
      const str1 = "Hey";
      const str2 = "Goodbye, friend!";
      const expectedStr1 = "Hey             "; // 15 spaces after "Hey"
      const expectedStr2 = "Goodbye, friend!";
      const [alignedStr1, alignedStr2] = alignLinesLeft(str1, str2);
      expect(alignedStr1).toBe(expectedStr1);
      expect(alignedStr2).toBe(expectedStr2);
    });
  
    it('should align when the first string is empty', () => {
      const str1 = "";
      const str2 = "World";
      const expectedStr1 = "     "; // 5 spaces
      const expectedStr2 = "World";
      const [alignedStr1, alignedStr2] = alignLinesLeft(str1, str2);
      expect(alignedStr1).toBe(expectedStr1);
      expect(alignedStr2).toBe(expectedStr2);
    });
  
    it('should align when the second string is empty', () => {
      const str1 = "Hello";
      const str2 = "";
      const expectedStr1 = "Hello";
      const expectedStr2 = "     "; // 5 spaces
      const [alignedStr1, alignedStr2] = alignLinesLeft(str1, str2);
      expect(alignedStr1).toBe(expectedStr1);
      expect(alignedStr2).toBe(expectedStr2);
    });
  
    it('should align when both strings are empty', () => {
      const str1 = "";
      const str2 = "";
      const expectedStr1 = "";
      const expectedStr2 = "";
      const [alignedStr1, alignedStr2] = alignLinesLeft(str1, str2);
      expect(alignedStr1).toBe(expectedStr1);
      expect(alignedStr2).toBe(expectedStr2);
    });
  
    it('should align strings with spaces correctly', () => {
      const str1 = "Hello ";
      const str2 = "World  ";
      const expectedStr1 = "Hello  ";
      const expectedStr2 = "World  ";
      const [alignedStr1, alignedStr2] = alignLinesLeft(str1, str2);
      expect(alignedStr1).toBe(expectedStr1);
      expect(alignedStr2).toBe(expectedStr2);
    });
  });